from django.contrib import admin
from .models import Patient

# Register your models here.


# admin.site.register(Patient)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        'last_name',
        'email',
        'tel',
        'ghana_card',
        'nhis_number',
    ]

    list_editable = [
        'email'
    ]

    list_filter = [
        'ghana_card'
    ]