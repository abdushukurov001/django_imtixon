from django import forms
from .models import BMI


class BMIForms(forms.Form):
    class Meta:
        form = BMI
        fields = ['height', 'kg']
        

