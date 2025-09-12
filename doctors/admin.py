from django.contrib import admin
from .models import Doctors

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('doctor_first_name', 'doctor_last_name', 'doctor_username')

    def doctor_first_name(self, obj):
        return obj.doctor_user.first_name

    def doctor_last_name(self, obj):
        return obj.doctor_user.last_name

    def doctor_username(self, obj):
        return obj.doctor_user.email
