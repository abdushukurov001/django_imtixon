from django.db import models


class BMI(models.Model):
    height = models.IntegerField()
    kg = models.IntegerField()


    class Meta:
        db_table = 'BMI'
        verbose_name = 'BMI'