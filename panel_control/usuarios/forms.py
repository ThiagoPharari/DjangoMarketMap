from django import forms

class LoginForm(forms.Form):
    username = forms.CharField( max_length= 255, widget= forms.TextInput (attrs= {'placeholder': 'Enter username'}))
    password = forms.CharField( max_length= 255, widget= forms.PasswordInput (attrs= {'placeholder': 'Enter password'}))