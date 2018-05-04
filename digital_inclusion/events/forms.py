from django import forms
from events.models import Event
from datetime import datetime
from django.contrib.admin import widgets

class EventInputForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['organization', 'name', 'start_time','end_time', 'description', 'mask_profile', 'contact_name', 'url']
        mask_profile = forms.Select(choices=("Yes", "No"))
        start_time = forms.DateTimeField(input_formats=["%Y/%m/%d %H:%M"])
        end_time = forms.DateTimeField(input_formats=["%Y/%m/%d %H:%M"])
        url = forms.URLField(required=False)
        labels = {
            'organization': 'Organization',
            'name': 'Name',
            'start_time': 'Event Start Time',
            'end_time': 'Event End Time',
            'description': 'Description',
            'mask_profile': 'Mask Profile?',
            'contact_name': 'Contact Name',
            'url': 'Event URL'
        }
        widgets = {
            'organization': forms.Select(attrs={'placeholder': 'Select Organization'}),
            'name': forms.TextInput(attrs={'placeholder': 'Event Name'}),
            # 'start_time': forms.DateTimeInput(format="%Y/%m/%d %H:%M"),
            # 'end_time': forms.DateTimeInput(format="%Y/%m/%d %H:%M"),
            # 'time': widgets.AdminSplitDateTime(),
            'description': forms.Textarea(attrs={'placeholder': 'Event Description'}),
            'contact_name': forms.TextInput(attrs={'placeholder': 'Name of contact'}),
            # 'url': forms.URLInput()
        }
