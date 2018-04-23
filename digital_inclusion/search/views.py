from django.shortcuts import render
from django.http import HttpRequest
from organization_management.models import Organization
from events.models import Event

# Create your views here.
def autocomplete(request: HttpRequest):
    query = request.GET.get("query", "")
    return render(request, template_name="autocomplete.jinja2", context={
        "org_results": Organization.objects.filter(name__icontains=query)[:10],
        "event_results": Event.objects.filter(name__icontains=query)[:10],
    })

def search(request:HttpRequest):
    query = request.GET.get("query", "")
    return render(request, template_name="search.jinja2", context={
        "org_results": Organization.objects.filter(name__icontains=query),
        "event_results": Event.objects.filter(name__icontains=query),
    })