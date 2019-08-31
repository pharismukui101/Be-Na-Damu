from django.db import models

# Create your models here.


class HealthInstituition(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Hotline = models.IntegerField(default=0)
    Location = models.CharField(max_length=200)
    Longtitude=models.FloatField(default=-34.2)
    Latitude=models.FloatField(default=42)

    def __str__(self):
        return self.Name


class HealthOfficial(models.Model):
    HealthInstituition = models.ForeignKey(
        HealthInstituition, on_delete=models.CASCADE)
    Password = models.CharField(max_length=200, default="Password")
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name
