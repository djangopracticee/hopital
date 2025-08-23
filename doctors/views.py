from django.shortcuts import render
from .models import Doctor

# Create your views here.

def dashboard(request):
    all_doctors = Doctor.objects.all()
    total_doctors = len(all_doctors)

    context = {
        'count': total_doctors,
    }



    return render(request, 'doctors/dashboard.html', context)