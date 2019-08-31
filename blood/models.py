from django.db import models
from health.models import HealthInstituition

# Creating models


class bloodData(models.Model):
    GroupRH = models.CharField(max_length=200)

    def __str__(self):
        return self.GroupRH


class BloodInstituition(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Hotline = models.IntegerField(default=0)
    Location = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class Request(models.Model):
    amount = models.FloatField(default=0)
    bloodData = models.ForeignKey(bloodData, on_delete=models.CASCADE)
    HealthOfficial = models.ForeignKey("health.HealthOfficial", related_name="healthO",
                                       on_delete=models.CASCADE)
    HealthInstituition = models.ForeignKey("health.HealthInstituition", related_name="healthI",
                                           on_delete=models.CASCADE, default=1)

    def getHealthLongtitude(self):
        longtitude=HealthInstituition.objects.get(pk=self.HealthInstituition)
        return longtitude

    # def getHealthLatitude(self):
    # return self.HealthOfficial.HealthInstituition.Longtitude

    def __str__(self):
        return "Request for " + str(self.amount) + " blood units"
