from django import forms
from .models import UserRegistration 

class registration_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = UserRegistration 
        fields = ['name', 'password', 'confirm_password', 'gender','email','mobile']
        

    def clean(self):
            cleaned_data = super(registration_form, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")
    
            if password != confirm_password:
                raise forms.ValidationError(
                    "password and confirm password does not match"
                )


class login_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserRegistration 
        fields = ['name', 'password']
