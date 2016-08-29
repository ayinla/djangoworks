from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Confession(models.Model):
     confession = models.CharField(max_length=300)
     id = models.AutoField(primary_key=True)
