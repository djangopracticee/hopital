from django.shortcuts import render


# Create your views here.

def opd_dashboard(request):
    return render(request, 'opd/dashboard.html')

