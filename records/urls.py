from django.urls import path
from . import views

app_name = 'records'



urlpatterns = [
    path('', views.records_dashboard, name='dashboard'),
    path('add-patient/', views.add_patient, name='add_patient'),
]

 
