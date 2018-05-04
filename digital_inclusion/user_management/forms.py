from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext as _
User = get_user_model()
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1", "password2")
        field_classes = {'username': UsernameField}

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(help_text="Needs to be a valid account email to send reset link.")

class PasswordResetForm(forms.ModelForm):
    security_answer = forms.CharField(max_length=512, strip=True)
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_("New Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean_security_answer(self):
        security_answer = self.cleaned_data.get("security_answer")
        if self.instance.security_answer.strip().lower() != security_answer:
            raise forms.ValidationError(
                "The security answer is incorrect"
            )
        return security_answer

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    class Meta:
        model = User
        fields = ['security_answer', 'password1', 'password2']