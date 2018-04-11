from django import forms
from django.contrib.postgres import forms as pgsql_forms
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from flagging.models import Flag


class FlagForm(forms.ModelForm):
    # def clean_contact_phone(self):
    #     contact_phone = self.cleaned_data['contact_phone']
    class Meta:
        model = Flag
        fields = ["issue", "other", "org_id"]
    org_id = forms.IntegerField()
    issue = forms.CharField(max_length=100)
    other = forms.CharField(max_length=2048, required=False)
