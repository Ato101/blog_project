from django.db import models
from datetime import datetime

class Features(models.Model):
    title= models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)



