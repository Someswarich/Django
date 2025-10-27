from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    employee_id=models.IntegerField
    department =models.CharField(max_length=50)
    salary=models.IntegerField


class Student(models.Model):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    age=models.IntegerField()
    roll_number=models.IntegerField()
