from django.db import models

# Create your models here.

class eequests(models.Model):
    bywho = models.CharField(max_length=120)
    uuid = models.CharField(max_length=120)
    
