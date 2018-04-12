from django.shortcuts import render, get_object_or_404, redirect
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET
from organization_management.models import Organization
from organization_management.forms import AddOrganizationForm
from django.conf import settings
import requests


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


@login_required()
@require_http_methods(['GET', 'POST'])
def add_organization(request: HttpRequest):
    if request.method == "POST":
        add_form = AddOrganizationForm(request.POST, request.FILES)
        if add_form.is_valid():
            organization = add_form.save()
            lat, lng = get_coord(add_form.cleaned_data["address"])
            organization.latitude = lat
            organization.longitude = lng
            organization.save()
            return redirect('orgs:view', pk=organization.pk)
    elif request.method == "GET":
        add_form = AddOrganizationForm()
    return render(request=request, template_name="create_organization.jinja2", context={'form': add_form})


def view_organization(request: HttpRequest, pk=None):
    organization = get_object_or_404(Organization, pk=pk)

    context = {'organization': organization, 'services': organization.services.all()}
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
