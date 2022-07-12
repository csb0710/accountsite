from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    account_id = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=5)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
