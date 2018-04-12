from django import forms
from events.models import Event
from datetime import datetime
from django.contrib.admin import widgets

class EventInputForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['organization', 'name', 'time', 'description', 'mask_profile', 'contact_name']
        mask_profile = forms.Select(choices=("Yes", "No"))
        labels = {
            'organization': 'Organization',
            'name': 'Name',
            'time': 'Event Time',
            'description': 'Description',
            'mask_profile': 'Mask Profile?',
            'contact_name': 'Contact Name'
        }
        widgets = {
            'organization': forms.Select(attrs={'placeholder': 'Select Organization'}),
            'name': forms.TextInput(attrs={'placeholder': 'Event Name'}),
            'time': forms.DateTimeInput(),
            # 'time': widgets.AdminSplitDateTime(),
            'description': forms.Textarea(attrs={'placeholder': 'Event Description'}),
            'contact_name': forms.TextInput(attrs={'placeholder': 'Name of contact'}),
        }
