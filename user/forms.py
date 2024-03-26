from django import forms
from django.core.exceptions import ValidationError
from .models import UserModel

class LoginForm(forms.Form):
    username = forms.CharField(max_length=222, widget=forms.TextInput(attrs={
        'placeholder':'username'
    }))
    password = forms.CharField(max_length=222, widget=forms.PasswordInput(attrs={
        'placeholder':'password'
    }))


    # class Meta:
    #     model = UserModel
    #     fields = ['username', 'password']
    #     widgets = {
    #         'username':forms.TextInput(attrs={
    #             'placeholder':'username',
    #         }),
    #         'password':forms.PasswordInput(attrs={
    #             'placeholder':'password',
    #         }),
    #     }

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=23, min_length=3, widget=forms.TextInput(attrs={
        'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Email'}))
    first_name = forms.CharField(max_length=23, widget=forms.TextInput(attrs={
        'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=23, widget=forms.TextInput(attrs={
        'placeholder':'Last Name'}))
    password = forms.CharField(max_length=23, min_length=8, widget=forms.PasswordInput(attrs={
        'placeholder':'Password'}))
    confirm_password = forms.CharField(max_length=23, min_length=8, widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password'}))
    
    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('parollar bir hil emas')
        return self.cleaned_data