from django.shortcuts import render, get_object_or_404, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET
from organization_management.models import Organization, Branch
from organization_management.forms import AddOrganizationForm, BranchForm, HoursFormset
from django.conf import settings
from django.utils import six
from django.core.files.storage import FileSystemStorage
from formtools.wizard.views import SessionWizardView
import requests
import os


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
    organizations = Organization.objects.all()
    context = {'organizations': organizations}
    return render(request=request, template_name="list_organizations.jinja2", context=context)


class OrganizationWizard(LoginRequiredMixin, SessionWizardView):
    file_storage = FileSystemStorage(location=settings.MEDIA_ROOT)
    form_list = [AddOrganizationForm, BranchForm]
    template_name = 'create_organization.jinja2'

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

    # def get_context_data(self, form, **kwargs):
    #     context = super(OrganizationWizard, self).get_context_data(form, **kwargs)
    #     if type(form) == BranchForm:
    #         context["hours_form"] = HoursFormset()
    #     return context
        
    def done(self, form_list, **kwargs):
        for form in form_list:
            if type(form) == AddOrganizationForm:
                organization: Organization = form.save()
            else:
                branch = form.save(commit=False)
                branch.organization = organization
                lat, lng = get_coord(form.cleaned_data["address"])
                branch.latitude = lat
                branch.longitude = lng
                branch.save()
                form.save_m2m()
        return redirect('orgs:view', pk=organization.pk)


def view_organization(request: HttpRequest, pk=None):
    branch = get_object_or_404(Branch, pk=pk)

    context = {'organization': branch.organization,
               'branch': branch}
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
