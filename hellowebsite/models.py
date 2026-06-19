from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField()
    email = models.CharField()
    address = models.CharField()
    
