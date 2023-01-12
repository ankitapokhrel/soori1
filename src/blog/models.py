from django.db import models

# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField() #verbose_name='image', width_field='width', height_field='height')  #upload_to=get_upload_to,