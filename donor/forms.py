from django import forms
from .models import Donor,Acknowledgement
from blood.models import Request

class donorForm(forms.Form):
    Name=forms.CharField()
    Gender=forms.CharField()
    DoB=forms.DateField()
    Weight=forms.FloatField()
    PhoneNo=forms.IntegerField()
    email=forms.CharField()
    donationAmount=forms.IntegerField()
    Location=forms.CharField()
    LastDonationDate=forms.DateField()
    bloodData=forms.CharField()

class DonorACK(forms.Form):
    class Meta:
        model=Donor,Request
        fields='__all__'