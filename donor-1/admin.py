from django.contrib import admin
from .models import Donor, Acknowledgement

# Register your models here.
admin.site.register(Donor)
admin.site.register(Acknowledgement)
