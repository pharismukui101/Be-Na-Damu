from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import hOfficerSignIn
from django.views import generic
from .models import HealthInstituition,HealthOfficial
from django.urls import reverse
from django.views.generic.edit import CreateView,UpdateView
from blood.models import Request
from donor.models import Acknowledgement,Donor
from django.http import HttpResponse,HttpResponseRedirect
import datetime

# Create your views here

class IndexView(FormView):
    model=HealthOfficial
    template_name="health/healthSignIn.html"
    form_class=hOfficerSignIn
    
    def get_success_url(self):
        return reverse('health:dashboard', kwargs={'hO_details.pk': hOfficial.id})
    
    def get_context_data(self, **kwargs):
        context= super(IndexView,self).get_context_data()
        context['hO_details']=HealthOfficial.objects.all()
        return context

class DashboardView(generic.DetailView):
    model= HealthOfficial
    #model= Request
    template_name="health/dashboard.html"
    context_object_name="hO_details"
    
    def get_context_data(self, **kwargs):
        context= super(DashboardView,self).get_context_data()
        context['hO_details']=HealthOfficial.objects.get(pk=self.kwargs['pk'])
        context['request_list']=Request.objects.all()
        context['donor_list']=Donor.objects.all()
        context['acknowledgement_list']=Acknowledgement.objects.all()
        return context
    
    def get_object(self):
        return HealthOfficial.objects.get(pk=self.kwargs['pk'])
    
    #def get_queryset(self):
        #return Request.objects.all()

class RequsitionView(CreateView):

    model=Request
    template_name="health/makeRequisition.html"
    fields='__all__'
    #["amount","bloodData"]
    context_object_name="request"

    def get_context_data(self, **kwargs):
        context= super(RequsitionView,self).get_context_data()
        context['hO_details']=HealthOfficial.objects.get(pk=self.kwargs['pk'])
        return context

  
class requestListView(generic.ListView):
    template_name="health/dashboard.html"
    context_object_name="request_list"

    def get_queryset(self):
        return Request.objects.all()#ignore error

def hOfficialDetails(request, hO_id):
    hO_details=HealthOfficial.objects.get(pk=hO_id)
    return render(request,'health/makeRequisition.html', {'hO_details': hO_details})

def deleteBloodRequest(request,pk,request_pk):
    b=Request.objects.get(id=request_pk)
    b.delete()
    return redirect(reverse('health:dashboard',args=(pk,)))

def updateDonorDonationDate(request,pk):
    Donor.objects.filter(id=int(request.POST.get('donors'))).update(LastDonationDate=datetime.date.today())
    return redirect(reverse('health:dashboard',args=(pk,)))
