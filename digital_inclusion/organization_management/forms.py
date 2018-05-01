from django import forms
from django.forms import inlineformset_factory, formset_factory
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from organization_management.models import Organization, Branch, OpeningHours


class BranchForm(forms.ModelForm):
    more_branches = forms.BooleanField(label="Add another branch?", required=False)    
    class Meta:
        model = Branch
        fields = ['address', 'contact_name',
                  'contact_email', 'contact_phone', 'languages', 'services', 'lab_machine_count',  'services_other', 'training_programs']
        labels = {
            'services_other': 'Other services',            
        }
        widgets = {            
            'address': forms.TextInput(attrs={'placeholder': 'Organization address'}),
            'contact_name': forms.TextInput(attrs={'placeholder': 'Name of contact'}),
            'contact_phone': PhoneNumberInternationalFallbackWidget(attrs={'placeholder': 'Phone number of contact', 'type': 'tel'}),
            'contact_email': forms.TextInput(attrs={'placeholder': 'Email of contact', 'type': 'email'}),
            'services': forms.SelectMultiple(attrs={'title':'Choose all that apply...',  'class': 'selectpicker'}),
            'languages': forms.SelectMultiple(attrs={'title':'Choose all that apply...',  'class': 'selectpicker'}),
            'training_programs': forms.SelectMultiple(attrs={'title':'Choose all that apply...',  'class': 'selectpicker'}),
            'lab_machine_count': forms.NumberInput(attrs={'placeholder': '20'}),
        }


class OpeningHoursForm(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = ['weekday', 'from_hour', 'to_hour']

class UserInputForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.data = kwargs.get("data", {"emails[]": []})
        if type(self.data) is list:
            self.emails = self.data.get("emails[]", [])
        return super().__init__(*args, **kwargs)


HoursFormset = inlineformset_factory(Branch, OpeningHours, form=OpeningHoursForm, extra=1)
class AddOrganizationForm(forms.ModelForm):
    # def clean_contact_phone(self):
    #     contact_phone = self.cleaned_data['contact_phone']
    def clean_logo_file(self):
        image = self.cleaned_data.get('logo_file', False)
        if image:
            if image._size > 4*1024*1024:
                raise forms.ValidationError("Image file too large ( > 4mb )")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")
    class Meta:
        model = Organization
        fields = ['name', 'description', 'website', 'logo_file', 'banner']
        labels = {
            'website': 'Website URL',
            'logo_file': 'Upload a logo',
            'banner': 'Upload a banner'
        }        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Organization name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Organization address'}),
            'website': forms.TextInput(attrs={'placeholder': 'http://example.com', 'type': 'url'}),
            'contact_name': forms.TextInput(attrs={'placeholder': 'Name of contact'}),
            'contact_phone': PhoneNumberInternationalFallbackWidget(attrs={'placeholder': 'Phone number of contact', 'type': 'tel'}),
            'contact_email': forms.TextInput(attrs={'placeholder': 'Email of contact', 'type': 'email'}),
            'services': forms.SelectMultiple(attrs={'title':'Choose all that apply...'}),
        }
