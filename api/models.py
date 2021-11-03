from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import datetime

# Create your models here.
# class Booking(models.Model):
    # id = models.BigAutoField(primary_key=True)


class Advisor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    photoUrl = models.URLField()

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null= False, blank=False)
    password = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=100, null=False)

class  Booking(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE, )