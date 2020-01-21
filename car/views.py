from django.shortcuts import render
from .models import Car

def all_cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars.html', {"cars":cars})