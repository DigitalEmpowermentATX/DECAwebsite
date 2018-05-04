from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render
from django.conf import settings
from organization_management.models import Organization, Branch
from events.models import Event
from main.models import UIComponent

# Create your views here.
def index(request: HttpRequest):
    featured_orgs = Organization.objects.exclude(banner__isnull=True).exclude(banner__exact="").order_by("?")[:3]
    return render(request, template_name="index.jinja2",context={
        "events": Event.objects.all(),
        "event_widget_options": {
            "show_header": False,
            "default_view": "listMonth"
        },
        "featured_orgs": featured_orgs,
        "content": UIComponent.objects.get(name="Index Content"),
        "resources": UIComponent.objects.get(name="Index Resources"),
        "highlights": UIComponent.objects.get(name="Index Highlights"),
    })

def about(request: HttpRequest):
    return render(request, template_name="about.jinja2", context={"content": UIComponent.objects.get(name="About")})

def map(request: HttpRequest):
    return render(request, template_name="map.jinja2", context={
        "gmaps_api_key": settings.GOOGLE_MAPS_JS_API_KEY,
        "orgs": Branch.objects.all()
    })