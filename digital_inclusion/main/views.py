from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render
from django.conf import settings
from organization_management.models import Organization, Branch
from events.models import Event

# Create your views here.
def index(request: HttpRequest):
    return render(request, template_name="index.jinja2",context={
        "events": Event.objects.all(),
        "event_widget_options": {
            "show_header": False,
            "default_view": "listMonth"
        }
    })

def about(request: HttpRequest):
    return render(request, template_name="about.jinja2")

def map(request: HttpRequest):
    return render(request, template_name="map.jinja2", context={
        "gmaps_api_key": settings.GOOGLE_MAPS_JS_API_KEY,
        "orgs": Branch.objects.all()
    })