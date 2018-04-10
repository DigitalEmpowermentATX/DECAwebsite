from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render
# Create your views here.
def index(request: HttpRequest):
    return render(request, template_name="index.jinja2")

def about(request: HttpRequest):
    return render(request, template_name="about.jinja2")

def map(request: HttpRequest):
    return render(request, template_name="map.jinja2")