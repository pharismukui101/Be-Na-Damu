from django import forms

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