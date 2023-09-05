from django.db import models

# Create your models here.
class Register(models.Model):
    account_no = models.IntegerField()
    name=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    balance=models.IntegerField(min('10000'))
    username=models.CharField(max_length=50)

    def __str__(self):
      return  self.name


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
       return self.username

