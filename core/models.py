from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, password=None, **extra_fields):
        """
        Create and return a regular user with a user_id and password.
        """
        if not user_id:
            raise ValueError('The User ID must be set')
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_superuser(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(user_id, password, **extra_fields)
        





class User(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('opd', 'OPD'),
        ('records', 'Records'),
        ('pharmacist', 'Pharmacist'),
        

    ]
    user_id = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES )
    
    username = None
    USERNAME_FIELD = "user_id"

    objects = CustomUserManager()


    


