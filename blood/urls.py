from django.urls import path
from . import views

app_name='blood'

urlpatterns=[
    path('',views.bloodDataView.as_view(), name='types'),
    path('instituition',views.bloodInstituitionView.as_view(), name='instituition'),
    #path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    #path('<int:pk>/result/',views.ResultView.as_view(),name="result"),
    #path('<int:question_id>/vote/',views.vote,name="vote"),
]