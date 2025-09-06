from django.urls import path
from . import views

app-name = 'doctor'

# base url : http://127.0.0.1:8000/

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]

