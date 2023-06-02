from django.db import models


# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=15)
    phone = models.BigIntegerField()
    is_blocked  = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(upload_to='images',default='images/user.jpg',max_length=300)
    id_proof = models.FileField(upload_to='documents',null= True)
    license  = models.FileField(upload_to='documents', null= True)
    



class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    balance = models.IntegerField()


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house_name = models.CharField(max_length = 100)
    street_name = models.CharField(max_length = 100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.IntegerField()
