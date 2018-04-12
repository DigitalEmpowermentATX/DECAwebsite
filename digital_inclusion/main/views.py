from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render
from django.conf import settings
from organization_management.models import Organization
# Create your views here.
def index(request: HttpRequest):
    return render(request, template_name="index.jinja2")

def about(request: HttpRequest):
    return render(request, template_name="about.jinja2")

def map(request: HttpRequest):
    return render(request, template_name="map.jinja2", context={
        "gmaps_api_key": settings.GOOGLE_MAPS_JS_API_KEY,
        "orgs": Organization.objects.all()
    })