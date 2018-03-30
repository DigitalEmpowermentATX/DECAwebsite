from django.shortcuts import render, get_object_or_404, redirect
from django.http.request import HttpRequest
from django.views.decorators.http import require_http_methods, require_GET
from organization_management.models import Organization
from organization_management.forms import AddOrganizationForm
# Create your views here.


@require_GET
def list_organization(request: HttpRequest):
    organizations = Organization.objects.all()
    context = {'organizations': organizations}
    return render(request=request, template_name="list_organizations.jinja2", context=context)


@require_http_methods(['GET', 'POST'])
def add_organization(request: HttpRequest):
    if request.method == "POST":
        add_form = AddOrganizationForm(request.POST)
        if add_form.is_valid():
            organization = add_form.save()
            return redirect('view_organization', pk=organization.pk)
    elif request.method == "GET":
        add_form = AddOrganizationForm()
    return render(request=request, template_name="create_organization.jinja2", context={'form': add_form})


def view_organization(request: HttpRequest, pk=None):
    organization = get_object_or_404(Organization, pk=pk)
    context = {'organization': organization}
    return render(request=request, template_name="view_organization.jinja2", context=context)


def flag_organization(request: HttpRequest):
    pass


def edit_organization(request: HttpRequest):
    pass
