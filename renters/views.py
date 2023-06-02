from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.contrib.auth.hashers import make_password
import jwt
from django.contrib.auth.hashers import check_password
from superuser.models import *
from .serializer import *
# Create your views here.




@api_view(['POST'])
def renter_signup(request):
    name = request.data['name']
    email = request.data['email']
    phone = request.data['phone']
    password = request.data['password']

    email_exist = Renters.objects.filter(email=email).exists()

    if email_exist:
        return Response({'status':'email already taken'})
    
    else:
        hashed_password = make_password(password)
        renter = Renters.objects.create(name = name, email = email, phone = phone, password = hashed_password)
        renter.save()
        return Response({'status':'renter created'})

@api_view(['POST'])
def renter_login(request):
    try:
        email = request.data['email']
        password = request.data['password']
    except:
        return Response({'status':'incorrect'})
    
    try:

        renter = Renters.objects.get(email = email)
        if check_password(password, renter.password):
            payload = {
                        'email' : renter.email,
                        'password' : renter.password,
            }
            renter_id = renter.id 
            jwt_token = jwt.encode(payload, 'secret', algorithm= 'HS256')
            return Response ({'status':'true', 'jwt_token':jwt_token, 'renter_id':renter_id})
        else:
            return Response({'status':'incorrect password'})
    except Renters.DoesNotExist:
        return Response({'status':'Incorrect '})
    
@api_view((['POST']))
def request_car(request,id):
    c= request.data['category']
    category = Category.objects.get(id=c)
    b = request.data['brand']
    brand = Brand.objects.get(id=b)
    name = request.data['name']
    ac = request.data['ac']
    fuel = request.data['fuel']
    rent = request.data['rent_price']
    description = request.data['description']
    image = request.data['image']
    image1 = request.data['image1']
    image2 = request.data['image2']
    image3 = request.data['image3']
    image4 = request.data ['image4']

    renters_car = Car.objects.create(category = category,
                                     brand = brand,
                                     name = name,
                                     ac = ac,
                                     fuel = fuel,
                                     rent_price = rent,
                                     description = description,
                                     image = image,
                                     image1 = image1,
                                     image2 = image2,
                                     image3 = image3,
                                     image4 = image4,
                                     renter_id = id
                                     )
    renters_car.save()
    return Response({'status':'Request send'})


@api_view(['GET'])
def get_car(request,id):
    car = Car.objects.filter(renter_id = id)
    serializer = RenterCarSerializer(car, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_car_request_details(request,id):
    car = Car.objects.get(id=id)
    print(car)
    serializer = RenterCarSerializer(car, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_booking_details(request,id):
    booked_cars = Booking.objects.filter(renter_id=id,status ='paid').select_related('car')
    print(booked_cars)
    serializer = BookingSerializer(booked_cars, many = True)
    print(serializer)
    return Response(serializer.data)



@api_view(['PATCH'])
def credit_wallet(request):
    id = request.data['id']
    change_status = Booking.objects.get(id=id)
    change_status.withdrawal_status = True
    change_status.save()
    renter_id = request.data['renter_id']
    renter = Renters.objects.get(id = renter_id)
    balance = request.data['revenue']
    try:
        wallet = Renter_Wallet.objects.get(renter = renter)
        wallet.balance += balance
        wallet.save()
    except Renter_Wallet.DoesNotExist:
        wallet = Renter_Wallet.objects.create(renter = renter, balance = balance)
        wallet.save()

    return Response({'status':'Money withdrawed'})


@api_view(['GET'])
def get_balance(request,id):
    renter = Renter_Wallet.objects.get(renter=id)
    serializer = WalletSerializer(renter, many = False)
    return Response(serializer.data)









    