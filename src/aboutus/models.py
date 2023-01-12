from django.db import models

# Create your models here.
class Ourteam(models.Model):
    name=models.CharField(max_length=30)
    position=models.CharField(max_length=20)
    image=models.ImageField()

class MessagefromCEO(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    image=models.ImageField()