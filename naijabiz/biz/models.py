from __future__ import unicode_literals
import hashlib
from django.db import models

# Create your models here.
class Biz(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    biztype= models.CharField(max_length=20)
    telephone = models.CharField(max_length=10)
    url = models.CharField(max_length=200, default="")
