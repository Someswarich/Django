from django.db import models

# Create your models here.
class Emp_data(models.Model):
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    role=models.CharField(max_length=100)




