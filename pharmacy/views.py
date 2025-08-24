from django.shortcuts import render

# Create your views here.

def pharma(request):
    return render(request, 'pharmacy/pharma.html')