from django.shortcuts import render
from django.http.request import HttpRequest


# Create your views here.

def list_organization(request: HttpRequest):
    pass


def showcase_organization(request: HttpRequest):
    pass


def add_organization(request: HttpRequest):
    if request.method == "GET":
        return render(request=request, template_name="create_organization.jinja2")
    elif request.method == "POST":
        pass


def view_organization(request: HttpRequest):
    pass
