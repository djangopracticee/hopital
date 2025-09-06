from django.db import models



# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    tel = models.CharField(max_length=10)
    ghana_card =models.CharField(max_length=50)
    nhis_number = models.PositiveBigIntegerField()
    date_of_birth = models.DateField()
    


    def __str__(self):
        return self.first_name + " " + self.last_name
