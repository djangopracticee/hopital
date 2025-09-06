from django.shortcuts import render
from .models import Doctor

# Create your views here.


def dashboard(request):

 
    return render(request, 'doctors/dashboard.html')