from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
from user_management.forms import RegistrationForm
User = get_user_model()
@require_http_methods(['POST', 'GET'])
def register(request: HttpRequest):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegistrationForm()
    return render(request, template_name="register.jinja2", context={'form': form})


def confirm(request: HttpRequest):
    pass


def forgot_password(request: HttpRequest):
    pass

