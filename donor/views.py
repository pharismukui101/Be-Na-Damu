from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.edit import CreateView, UpdateView
from .models import Donor, Acknowledgement
from blood.models import bloodData
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django import forms
from django.db import models
import datetime
from .forms import donorForm
from blood.models import Request
from health.models import HealthInstituition

# Create your views here.


class DonorCreate(CreateView):
    model = Donor
    template_name = "donor/index_form.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse('donor:dashboard', kwargs={'pk': self.object.pk})


class DonorUpdate(UpdateView):
    model = Donor
    template_name = "donor/donor_update.html"
    fields = '__all__'
    context_object_name = 'update_donor'

    def get_success_url(self):
        return reverse('donor:dashboard', kwargs={'pk': self.object.pk})


class DashboardView(generic.DetailView):
    model = Donor
    template_name = "donor/dashboard.html"
    context_object_name = "donor_details"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data()
        context['request_list'] = Request.objects.all()
        context['HInstituition_list']=HealthInstituition.objects.all()
        return context

    def get_object(self):
        return Donor.objects.get(pk=self.kwargs['pk'])


def successfulSubmission(request):
    return reverse('successHTML')





def donorAcknowledgement(request,pk):
    donors=Donor(id=request.POST.get('donors'))
    requests=Request(id=request.POST.get('requests'))
    Acknowledgement.objects.create(donor=donors,Request=requests)
    #d.save()
    return redirect(reverse('donor:dashboard',args=(pk,)))
    #return HttpResponse("donors "+str(donors)+" requests "+str(requests))

#def getDonorAcknowledgement(post_data):
    #data=post_data.copy()
    #donorAcknowledgement={
    #    'donor':data.get['donors'],
    #    'Request':data.get['requests']
    #}
    #return donorAcknowledgement