from django.shortcuts import render, get_object_or_404, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods, require_GET
from organization_management.models import Organization, Branch, ActivationToken
from organization_management.forms import AddOrganizationForm, BranchForm, HoursFormset, UserInputForm
from django.conf import settings
from django.utils import six
from django.core.files.storage import FileSystemStorage
from formtools.wizard.views import SessionWizardView
import requests
import os
from events.models import Event
from django.core.mail import send_mail
import re
from concurrent.futures import ThreadPoolExecutor, wait


def valid_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


# Create your views here.


def get_coord(address):
    gmaps_api_url = "https://maps.googleapis.com/maps/api/geocode/json"
    resp = requests.get(gmaps_api_url,
                        params={
                            "address": address,
                            "key": settings.GOOGLE_MAPS_API_KEY
                        }).json()
    location = resp["results"][0]["geometry"]["location"]
    return (location["lat"], location["lng"])


@require_GET
def list_organization(request: HttpRequest):
    branches = Branch.objects.all()
    context = {'branches': branches}
    return render(request=request, template_name="list_organizations.jinja2", context=context)


class OrganizationWizard(LoginRequiredMixin, SessionWizardView):
    file_storage = FileSystemStorage(location=settings.MEDIA_ROOT)
    form_list = [AddOrganizationForm, BranchForm, UserInputForm]
    # form_list = [UserInputForm]
    template_name = 'create_organization.jinja2'
    TEMPLATES = {"0": "create_organization.jinja2",
                 "1": "create_organization.jinja2",
                 "2": "add_users.jinja2"}

    # TEMPLATES = {"0": "add_users.jinja2"}

    def get_template_names(self):
        return [self.TEMPLATES[self.steps.current]]

    def get_form_list(self):
        step = self.storage.current_step
        prev_data = self.get_cleaned_data_for_step(step) or {}
        if prev_data and prev_data.get('more_branches') == True:
            keys = list(self.form_list.keys())
            index = keys.index(step) + 1
            key = "more_branches-{0}".format(index)
            self.form_list[key] = BranchForm
        form_list = super().get_form_list()
        return form_list

    def done(self, form_list, **kwargs):
        branch = None
        organization = None
        for form in form_list:
            if type(form) is AddOrganizationForm:
                organization: Organization = form.save()
            elif type(form) is BranchForm:
                branch = form.save(commit=False)
                branch.organization = organization
                lat, lng = get_coord(form.cleaned_data["address"])
                branch.latitude = lat
                branch.longitude = lng
                branch.save()
                form.save_m2m()
            elif type(form) is UserInputForm:
                emails = form.data.getlist("emails[]")
                valid_emails = list(filter(valid_email, emails))
                tokens = [ActivationToken.for_organization(organization) for email in valid_emails]
                for token in tokens:
                    token.save()

                def activation_email(email, token):
                    msg_html = render_to_string('email_template.jinja2', {'organization': organization,
                                                                          'token': token})
                    send_mail(subject="You Have Been Invited to {}'s DECA Site".format(organization.name),
                              html_message=msg_html,
                              from_email=settings.DEFAULT_FROM_EMAIL,
                              recipient_list=[email],
                              fail_silently=False)

                with ThreadPoolExecutor(max_workers=10) as email_pool:
                    futures = []
                    for email, token in zip(valid_emails, tokens):
                        f = email_pool.submit(activation_email, email, token)
                        futures.append(f)
                    wait(futures)


        return redirect('orgs:view', pk=branch.pk)
        # return redirect('orgs:view')


def view_organization(request: HttpRequest, pk=None):
    branch = get_object_or_404(Branch, pk=pk)

    context = {'organization': branch.organization,
               'branch': branch,
               "events": Event.objects.filter(organization=branch.organization),
               "event_widget_options": {
                   "show_header": False,
                   "default_view": "listMonth"
               },
               "gmaps_api_key": settings.GOOGLE_MAPS_JS_API_KEY,
               "orgs": Branch.objects.filter(organization=branch.organization)}
    return render(request=request, template_name="view_organization.jinja2", context=context)


@login_required()
@require_http_methods(['GET', 'POST'])
def edit_organization(request: HttpRequest, pk=None):
    organization = get_object_or_404(Organization, pk=pk)
    if request.method == "POST":
        edit_form = AddOrganizationForm(request.POST, instance=organization)
        if edit_form.is_valid():
            organization = edit_form.save()
            return redirect('orgs:view', pk=organization.pk)
    elif request.method == "GET":
        edit_form = AddOrganizationForm(instance=organization)
    return render(request=request, template_name="edit_organization.jinja2",
                  context={'form': edit_form, 'organization': organization})


@login_required()
@require_http_methods(['GET', 'POST'])
def add_users(request: HttpRequest, pk=None):
    return render(request, template_name="add_users.jinja2")
