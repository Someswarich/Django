from django.db import models


class Users(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.CharField(max_length=100)
    mobile_no=models.IntegerField(max_length=10,unique=True)
    


# Create your models here.
