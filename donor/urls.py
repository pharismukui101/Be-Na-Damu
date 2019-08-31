from django.urls import path,re_path
from django.http import HttpResponse,HttpResponseRedirect
from . import views

app_name='donor'

urlpatterns=[
    path('',views.DonorCreate.as_view(), name='index'),
    #re_path(r'^/$',views.DonorCreate.as_view(), name='re-index'),
    path('<int:pk>/',views.DashboardView.as_view(), name='dashboard'),
   # re_path(r'^(?P<pk>[0-9]+)/$',views.DashboardView.as_view(), name='re-dashboard'),
   # re_path(r'^(?P<pk>[0-9]+)/update $', views.DonorUpdate.as_view(), name='re-update'),
    path('<int:pk>/update', views.DonorUpdate.as_view(),name='update'),
    path('<int:pk>/accept',views.donorAcknowledgement,name='accept'),
    #re_path(r'^(?P<pk>[0-9]+)/accept $',views.donorAcknowledgement,'re-accept'),
    #path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    #path('<int:pk>/result/',views.ResultView.as_view(),name="result"),
    #path('<int:question_id>/vote/',views.vote,name="vote"),
]