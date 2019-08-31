from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .models import Request, BloodInstituition,bloodData
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
class bloodDataView(generic.ListView):
    template_name="blood/bloodData.html"
    context_object_name="full_blood_list"

    def get_queryset(self):
        return bloodData.objects.all()#ignore error

class bloodInstituitionView(generic.ListView):
    template_name="blood/bloodInstituition.html"
    context_object_name="full_bloodInstituition_list"

    def get_queryset(self):
        return BloodInstituition.objects.all()#ignore error