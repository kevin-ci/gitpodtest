from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=24)
    car_model = models.CharField(max_length=50)
    registration = models.CharField(max_length=12)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.registration