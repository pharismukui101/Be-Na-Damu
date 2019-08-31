from django import forms
from.models import HealthOfficial
from django.urls import reverse

class hOfficerSignIn(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
    
    #class Meta:
      