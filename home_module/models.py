from django.db import models

# Create your models here.
class mypic(models.Model):
    title=models.CharField(max_length=200,verbose_name='عنوان')
    photo=models.ImageField(upload_to='image')

