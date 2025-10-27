from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10,unique=True,primary_key=True)
    document=models.FileField(upload_to='documents/')
