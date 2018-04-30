from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
User = get_user_model()
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1", "password2", "security_question", "security_answer")
        field_classes = {'username': UsernameField}