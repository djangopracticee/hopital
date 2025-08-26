from django.shortcuts import render
from doctors.models import Doctor

# Create your views here.


def patients(request):
    number_of_doctors = Doctor.objects.all().count()
    doctors = Doctor.objects.all()

    # number_of_doctors = 3
    # doctors = [{emma, kumi, k@gmail.com }, {fred, mensah, fred@gmail.com}, {sARA, SAM, SAM@gmail.com }]


    context = {
        "num": number_of_doctors,
        "doctors": doctors,
    }

    return render(request, 'patients/dashboard.html', context)