from django.contrib import admin
from .models import HealthInstituition,HealthOfficial

# Register your models here.
admin.site.register(HealthInstituition)
admin.site.register(HealthOfficial)