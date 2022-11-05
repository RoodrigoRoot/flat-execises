import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name="phone number", max_length=10)
    property_id = models.CharField(max_length=200)
