from django.shortcuts import render
from .models import BMI


def home_view(request):
    obj = BMI.objects.all()
    print('qqwqwqw')
    return render(request, 'home.html', context={
        obj:'obj'
    })