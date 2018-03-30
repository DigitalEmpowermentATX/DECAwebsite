from django import forms
from organization_management.models import Organization
class AddOrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description', 'website', 'contact_name', 'contact_phone', 'key_employees']
