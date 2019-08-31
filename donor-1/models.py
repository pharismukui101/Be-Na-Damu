from django.db import models
from django.utils import timezone
import datetime
from health.models import HealthInstituition

# Create your models here.


class Donor(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

    Name = models.CharField(max_length=200)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    DoB = models.DateField('date born')
    Weight = models.FloatField(default=0)
    PhoneNo = models.IntegerField(default=0)
    email = models.CharField(max_length=200)
    donationAmount = models.IntegerField(
        default=500, verbose_name="Donation Amount")
    Location = models.CharField(max_length=200)
    LastDonationDate = models.DateField('last Donation Date')
    bloodData = models.ForeignKey("blood.bloodData", verbose_name="blood Data", related_name="blood",
                                  on_delete=models.CASCADE)

    def __str__(self):
        if (self.Gender == "Male"):
            return "Mr. " + self.Name
        else:
            return "Miss/Mrs. " + self.Name

    def CheckWeight(self):
        eligibleWeight = self.Weight > 50
        return eligibleWeight

    def checkAge(self):
        now = timezone.now().date()
        age = int((now-self.DoB).days/365.25)
        return 65 >= age >= 16

    def checkLastDonationPeriod(self):
        now = timezone.now().date()
        if (self.Gender == 'Male'):
            period = int((now - self.LastDonationDate).days)
            return period >= 90
        else:
            period = int((now - self.LastDonationDate).days)
            return period >= 120

        
    def checkEligibility(self):
        if (self.checkAge and self.CheckWeight  and self.checkLastDonationPeriod):
            return True
        else:
            return False


class Acknowledgement(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    Request = models.ForeignKey(
        "blood.Request", related_name="blood", on_delete=models.CASCADE)
