from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    contact_no:models.CharField(max_length=20)
    address=models.TextField()
    email=models.EmailField(unique=True)
    link=models.URLField(max_length=200)
    
