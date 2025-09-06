from django.urls import path
from . import views


# base url : http://127.0.0.1:8000/patients/patients

urlpatterns = [
    path('', views.patients, name='doctors'),
]

