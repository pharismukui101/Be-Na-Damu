from django.contrib import admin
from .models import bloodData, BloodInstituition,Request
# Register your models here.
admin.site.register(bloodData)
admin.site.register(BloodInstituition)
admin.site.register(Request)