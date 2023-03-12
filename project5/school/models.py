from django.db import models

# Create your models here.

class student(models.Model):
    School = models.CharField(max_length=100)
    Sex = models.CharField(max_length=50)
    Age = models.IntegerField()
    Mjob = models.CharField(max_length=100)
    Fjob = models.CharField(max_length=100)
    Reason = models.CharField(max_length=100)
    Guardian = models.CharField(max_length=100)
    Paid = models.CharField(max_length=100)
    
