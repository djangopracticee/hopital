from django.shortcuts import render


# Create your views here.

def records_dashboard(request):
    return render(request, 'records/dashboard.html')


def add_patient(request):
    return render(request, 'records/add_patient.html')
