import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from events.forms import EventInputForm
from organization_management.models import Organization
# Create your views here.


def add(request):
    if request.method == "POST":
        f = EventInputForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("Success!")
    elif request.method == "GET":
        f = EventInputForm()
    return render(request,
                  template_name="event_input.jinja2",
                  context={"form": f})


def calendar(request):
    return HttpResponse("Events Page")
