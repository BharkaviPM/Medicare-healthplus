from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    expiry_date = models.DateField()

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    available_today = models.BooleanField(default=True)
    available_time = models.CharField(max_length=100, blank=True)

class Appointment(models.Model):
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class VirtualAssistance(models.Model):
    problem = models.CharField(max_length=200)
    first_aid = models.TextField()
