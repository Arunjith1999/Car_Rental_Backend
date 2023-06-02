from django.db import models


# Create your models here.



class Renters(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 40)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=130)
    is_created = models.DateTimeField(auto_now_add= True)
    is_updated = models.DateTimeField(auto_now_add= True)
    
# class Rent_cars(models.Model):

#     orderStatus =[
#         ('pending','pending'),
#         ('Accepted','Accepted'),
#         ('Rejected', 'Rejected')
#     ]
#     renter = models.ForeignKey(Renters, on_delete=models.CASCADE ,null=True, default=None)
#     name = models.CharField(max_length=30)
#     category = models.CharField(max_length= 30, null=True)
#     brand = models.CharField(max_length = 30, null= True)
#     fuel_type = models.CharField(max_length=30)
#     rent = models.IntegerField(default=500)
#     car_documents = models.FileField()
#     ac = models.CharField(default='Yes', max_length=10)
#     description = models.TextField(max_length= 1024 ,default= '')
#     image = models.ImageField(upload_to = 'images')
#     image1 = models.ImageField(upload_to = 'images',default='images/Harrier.jpg')
#     image2 = models.ImageField(upload_to = 'images',default='images/Harrier.jpg')
#     image3 = models.ImageField(upload_to='images',default='images/Harrier.jpg')
#     image4 = models.FileField(upload_to='documents',null=True)
#     status = models.CharField(choices=orderStatus, default='pending')


class Renter_Wallet(models.Model):
    renter = models.ForeignKey(Renters, on_delete=models.CASCADE)
    balance = models.IntegerField()