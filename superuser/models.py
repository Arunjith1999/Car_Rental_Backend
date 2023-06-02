from django.db import models
from  users.models import *
from renters.models import *

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
class Brand(models.Model):
    Category = models.ForeignKey(Category,on_delete = models.CASCADE)
    title = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    # def __str__(self):
    #     return self.title

class Car(models.Model):

    status = [
        ('verifying','verifying'),
        ('accepted','accepted'),
        ('rejected','rejected')
    ]
    name = models.CharField(max_length = 30)
    renter = models.ForeignKey(Renters, on_delete=models.CASCADE ,null=True, default=None)
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'images')
    image1 = models.ImageField(upload_to = 'images',default='images/Harrier.jpg')
    image2 = models.ImageField(upload_to = 'images',default='images/Harrier.jpg')
    image3 = models.ImageField(upload_to='images',default='images/Harrier.jpg')
    image4 = models.FileField(upload_to='documents',null=True)
    fuel = models.CharField(max_length = 20, default='Petrol')
    rent_price = models.IntegerField(default = 100)
    description = models.TextField(max_length= 1024 ,default= '')
    ac = models.CharField(max_length=20, default= 'Yes')
    location = models.CharField(max_length = 100, null=True)
    is_accepted = models.CharField(max_length=30, choices=status,default = 'verifying')

    # def __str__(self):
    #     return self.name
    

class Booking(models.Model):
    Razor_Pay ='Razor_Pay'
    Wallet  =  'Wallet'
    PAYMENT_METHOD=[
        (Razor_Pay, 'Razor_Pay'),
        (Wallet, 'Wallet')
    ]
    paid = 'paid'
    cancelled = 'cancelled'
   
    
    status =[
        (paid,'paid'),
        (cancelled,'cancelled'),
       

    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renters, on_delete=models.CASCADE ,null=True)
    withdrawal_status = models.BooleanField(default= False)
    start_date = models.DateTimeField(null= True)
    end_date = models.DateTimeField(null=True)
    rent    = models.IntegerField(null=True)
    total_rent = models.IntegerField()
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD,default=Razor_Pay)
    transaction_id = models.CharField()
    status = models.CharField(choices=status,default=paid)
    is_updated = models.DateTimeField(auto_now=True)
    is_created = models.DateTimeField(auto_now_add=True)