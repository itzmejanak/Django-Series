from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    desc = models.TextField()

