from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = (models.CharField(max_length=128))


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #user = 
    employee_id = models.CharField(max_length=10, unique=True)
    is_staff = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username


class Incharge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    incharge_id = models.CharField(max_length=10, unique=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
