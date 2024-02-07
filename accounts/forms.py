from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


def check_length(value):
    if len(value)<3:
        raise ValidationError('Password too short or fields are empty')


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(validators=[EmailValidator('Enter a valid email address.')])
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, validators=[check_length])
    repeat_password = forms.CharField(max_length=50, widget=forms.PasswordInput,  validators=[check_length])
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("repeat_password")
        if p1 != p2:
            raise forms.ValidationError("Passwords don't match")

