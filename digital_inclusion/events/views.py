import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from events.forms import EventInputForm

# Create your views here.
def add(request):
    if request.method == "GET":
        f = EventInputForm()
        return render(request,
                      template_name="event_input.jinja2",
                      context={"form": f})
    elif request.method == "POST":
        f = EventInputForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("Success!")
        else:
            return HttpResponse(json.dumps([str(x) for x in f.errors]))

def calendar(request):
    return HttpResponse("Events Page")
