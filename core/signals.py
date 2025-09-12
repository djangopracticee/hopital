from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from doctors.models import Doctors

User = settings.AUTH_USER_MODEL   # reference the custom user

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created and instance.role == "doctor":
        Doctors.objects.create(doctor_user=instance)

