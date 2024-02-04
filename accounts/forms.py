from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("repeat_password")
        if p1 is None or p2 is None or p1 != p2:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data
