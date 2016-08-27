from __future__ import unicode_literals
import hashlib
from django.db import models

# Create your models here.
class Biz(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    biztype= models.CharField(max_length=20)
    telephone = models.CharField(max_length=10)
