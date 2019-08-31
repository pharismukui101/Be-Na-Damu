from django.urls import path
from . import views

app_name='health'

urlpatterns=[
    path('',views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DashboardView.as_view(), name='dashboard'),
    #path('<int:pk>/', views.requestListView.as_view()),
    path('<int:pk>/request/',views.RequsitionView.as_view(),name="request"),
    path('<int:pk>/updateDonor/',views.updateDonorDonationDate,name="updateDonor"),
    path('<int:pk>/delete/<int:request_pk>',views.deleteBloodRequest,name="deleteRequest"),
    #path('<int:pk>/request/',views.hOfficialDetails),
    #path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    #path('<int:pk>/result/',views.ResultView.as_view(),name="result"),
    #path('<int:question_id>/vote/',views.vote,name="vote"),
]