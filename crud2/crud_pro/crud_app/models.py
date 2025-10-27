from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    department=models.CharField(max_length=30)
