from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import User
import jwt
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from superuser.serializer import *
from .serializer import *
from datetime import datetime, date
from django.utils import timezone
from pytz import timezone as tz
import uuid
from django.conf import settings
import razorpay
# Create your views here.


@api_view(["POST"])
def user_signup(request):
    first_name = request.data['firstName']
    last_name = request.data['lastName']
    email = request.data['email']
    phone1 = str(request.data['phonenumber'])
    phone = '91'+phone1
    password = request.data['password']
    
    exists =  User.objects.filter(email=email).exists()
    data = {'exists':exists}
    
    if exists:
        return Response(data)
      

    else:
            user = User.objects.create(first_name = first_name,
                                    last_name = last_name,
                                    email = email,
                                    phone = phone,
                                    password = password,
                                    )
            
            user.save()
            return Response({'status':'true'})
   


@api_view(['POST'])
def user_login(request):
    try:
        email = request.data['email']
        password = request.data['password']

    except:
        return Response({'status': ' Incorrect' })
    
    try :
        user = User.objects.get(email = email , password = password, is_blocked = False)
        
        payload ={'email': user.email,
                  'password' : user.password,
                  'username':user.first_name
                  }
        user_id =user.id
        jwt_token = jwt.encode(payload,'secret',algorithm = 'HS256')
        return Response({'status':'true','jwt_token':jwt_token,'user_id':user_id})
    except User.DoesNotExist:
        return Response({'status':'does not exist'})
    

@api_view(['POST'])
def forget_password(request):
    print(request.data,'.......')
    try:
        phone = request.data['phone']

    except:
        return Response({'status':'incorrect'})
    
    try:
        print('otp.....')
        user = User.objects.get(phone = phone)
        print(user)
        payload ={'email':user.email,
                  'phone':user.phone }
        user_id = user.id
        jwt_token = jwt.encode(payload, 'secret',algorithm= 'HS256')
        return Response({'status':'verified','jwt_token':jwt_token,'user_id':user_id})
    except:
        return Response({'status':'Number Does Not Registered'})


  


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    print('jxjxjx')
    request.user.auth_token.delete()
    logout(request)
    return Response({'status':'userloggedout'})


@api_view(['GET'])
def user_profile(request, id):
    user = User.objects.get(id = id)
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data)


@api_view(['GET'])
def user_address(request,id):
    try:
        address = Address.objects.get(id=id)
        serializer = AddressSerializer(address, many = False)
        return Response(serializer.data)
    except Address.DoesNotExist:
        return Response({'status':'Not Exist'})
        

@api_view(['PUT'])
def add_profile_pic(request, id):
    user = User.objects.get(id = id)
    profile_pic = request.data['profile_pic']
    user.profile_pic = profile_pic
    user.save()
    return Response({'status':'profile_pic Added'})

@api_view(['PUT'])
def add_id_proof(request, id):
    user = User.objects.get(id =id)
    id_proof = request.data['id_proof']
    user.id_proof = id_proof
    user.save()
    return Response({'status':'id_proof updated'})

@api_view(['PUT'])
def add_license(request,id):
    user = User.objects.get(id =id)
    license = request.data['license']
    user.license = license
    user.save()
    return Response({'status':'license updated'})


# @api_view(['GET'])
# def get_location(request):
#     location = Locations.objects.all()
#     serializer = LocationSerializer(location , many = True)
#     return Response(serializer.data)


@api_view(['POST'])
def booking_details(request):
    start_date = datetime.strptime(request.data['startDate'], '%Y-%m-%d %I:%M %p')
    print(start_date,'../././/.///.//./././/.//')
    end_date = datetime.strptime(request.data['endDate'], '%Y-%m-%d %I:%M %p')
    carId = request.data['carId']
    car = Car.objects.get(id = carId)
    rent = car.rent_price
    location = car.location
    time_difference = end_date - start_date
    difference_in_days = time_difference.days
    Total_rent = difference_in_days * rent
    return Response ({'rent':rent,'difference_in_days':difference_in_days,'Total_rent':Total_rent, 'location':location})
    

@api_view(['POST'])
def confirm_booking(request):
    client = razorpay.Client(
        auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET)
    )
    print(request.data,'///////')
    u = request.data['user_id']
    user_id = User.objects.get(id=u)
    c = request.data['data']['carId']
    car_id = Car.objects.get(id=c)
    transaction_id = str(uuid.uuid4())
    rent  = request.data['details']['rent']
    total_rent = request.data['details']['Total_rent']
    startDate_str = request.data['data']['startDate'].strip('\"')
    startDate = datetime.strptime(startDate_str,'%Y-%m-%d %I:%M %p')
    formatted_startDate = startDate.strftime('%Y-%m-%d %H:%M:%S%z')
    endDate_str = request.data['data']['endDate'].strip('\"')
    endDate = datetime.strptime(endDate_str,'%Y-%m-%d %I:%M %p')
    formatted_endDate = endDate.strftime('%Y-%m-%d %H:%M:%S%z')

    booked = Booking.objects.create(user = user_id,
                                    car = car_id,
                                    start_date = formatted_startDate,
                                    end_date = formatted_endDate,
                                    transaction_id = transaction_id,
                                    rent = rent,
                                    total_rent = total_rent,
                                    )
    booked.save()
    return Response({'status':'Booking Confirmed'})

@api_view(['GET'])
def get_booking_history(request, id):
    history = Booking.objects.filter(user_id=id).select_related('car')
    serializer = BookingSerializer(history, many=True)
    return Response({'ser1': serializer.data})


@api_view(['GET'])
def get_booked_dates(request, id):
    cars = Booking.objects.filter(car_id=id,status = 'paid')
    car_dates = []

    for car in cars:
        car_dates.append({
            'start_date': car.start_date.strftime('%Y-%m-%d %H:%M:%S'),
            'end_date': car.end_date.strftime('%Y-%m-%d %H:%M:%S')
        })   
    return Response({'date':car_dates})


@api_view(['PATCH'])
def cancel_payment(request):
    id = request.data['id']
    cancel = Booking.objects.filter(id=id)
    cancel.update(status='cancelled')
   
    user1 = request.data['user_id']
    user = User.objects.get(id=user1)
    balance = request.data['rent']
    print(balance)
    try:
        wallet = Wallet.objects.get(user=user)
        wallet.balance += balance
        print(wallet.balance)
        wallet.save()  # Save the updated balance
    except Wallet.DoesNotExist:
        wallet = Wallet.objects.create(user=user, balance=balance)
        wallet.save()
    return Response({'status': 'cancelled'})


@api_view(['GET'])
def profile_status(request, id):
    user  = User.objects.get(id = id)
    print(user.profile_pic)
    print(user.id_proof)
    if user.license == '' or user.id_proof == '':
        print('false')
        return Response({'status':'false'})
    else:
        print('true')
        return Response({'status': 'true'})


@api_view(['GET'])
def wallet_balance(request,id):
    avail_bal = Wallet.objects.get(user = id)
    serializer = WalletSerializer(avail_bal, many = False)
    return Response(serializer.data)



@api_view(['POST'])
def add_address(request, id):
    user_id = User.objects.get(id=id)
    house_name = request.data['house_name']
    street_name = request.data['street_name']
    state_name = request.data['state_name']
    country = request.data['country']
    zipcode = request.data['zipcode']

    address = Address.objects.create(user=user_id,
                                     house_name=house_name,
                                     state=state_name,
                                     street_name = street_name,
                                     country = country,
                                     zipcode = zipcode
                                     )
    address.save()
    return Response({'status':'Address Added'})




        
    
    

    
    
    

