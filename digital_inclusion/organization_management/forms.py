from django import forms
from django.contrib.postgres import forms as pgsql_forms
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from organization_management.models import Organization


class AddOrganizationForm(forms.ModelForm):
    # def clean_contact_phone(self):
    #     contact_phone = self.cleaned_data['contact_phone']

    class Meta:
        model = Organization
        fields = ['name', 'description', 'website', 'contact_name',
                  'contact_email', 'contact_phone', 'logo_file', 'services']
        labels = {
            'website': 'Website URL',
            'logo_file': 'Upload a logo'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Organization Name'}),
            'description': forms.Textarea(attrs={'placeholder': "Description of your organization", 'rows': 5}),
            'website': forms.TextInput(attrs={'placeholder': 'Link to your website', 'type': 'url'}),
            'contact_name': forms.TextInput(attrs={'placeholder': 'Name of Contact'}),
            'contact_phone': PhoneNumberInternationalFallbackWidget(attrs={'placeholder': 'Phone Number of Contact', 'type': 'tel'}),
            'contact_email': forms.TextInput(attrs={'placeholder': 'Email of Contact', 'type': 'email'}),
            'services': forms.SelectMultiple(attrs={'title':'Choose all that apply...'}),
        }
