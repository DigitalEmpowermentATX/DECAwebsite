import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from events.forms import EventInputForm
from organization_management.models import Organization
from events.models import Event
from django.http import HttpResponseRedirect


# Create your views here.


def add(request):
    if request.method == "POST":
        f = EventInputForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect("events:calendar")
    elif request.method == "GET":
        f = EventInputForm()
    return render(request,
                  template_name="event_input.jinja2",
                  context={"form": f})


def calendar(request):
    return render(request, template_name="calendar.jinja2", context={
        "events": Event.objects.all(),
        "event_widget_options": {
            "show_header": True,
            # "default_view": "listMonth"
        }
    })
