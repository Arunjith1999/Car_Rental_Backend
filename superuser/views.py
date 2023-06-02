from django.shortcuts import render
import jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  django.contrib.auth.models import User as Admin_user
from .models import Category
from users.models import *
from .serializer import *
from urllib.parse import quote
from datetime import date
import datetime
from django.db.models import Count,Q
from django.contrib.auth.hashers import check_password


# Create your views here.

@api_view(['POST'])
def admin_login(request):
    try:
        email = request.data['email']
        password = str(request.data['password'])
    except:
        return Response({'status': 'Incorrect'})
    try:
        admin = Admin_user.objects.get(email = email)
        if check_password(password,admin.password):
            payload = {'email' : admin.email,
                     'password' : admin.password,
                    }
            admin_id = admin.id 
            jwt_token = jwt.encode(payload, 'secret' ,algorithm= 'HS256')
            return Response({'status':'true','jwt_token':jwt_token, 'admin_id':admin_id})
        else:
            return Response({'status':'incorrect'})
    except Admin_user.DoesNotExist:
        return Response({'status':'incorrect111'})
    

@api_view(['GET'])
def Get_Category(request):
   
    category = Category.objects.all() 
    serializer = CategorySerializer(category,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def brands(request,id):
    print('vannu....')
    brand = Brand.objects.filter(Category=id).order_by('title')
    serializer = BrandSerializer(brand, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def brand(request):
    brand = Brand.objects.all().distinct('title')
    serializer = BrandSerializer(brand, many = True)
    return Response(serializer.data)



@api_view(['GET'])
def car_models(request,id):
    car_type = Car.objects.filter(category = id,is_accepted='accepted')
    # category_name = car_type.category.title
    serializer = CarSerializer(car_type, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def car_details(request,id):
    car_detail = Car.objects.get(id = id)
    serializer = CarSerializer(car_detail, many = False)
    return Response(serializer.data)


      
        
    
@api_view(['GET'])
def car_brands(request,id,brand_id):
    print(id,brand_id)
    car_brand = Car.objects.filter(category = id,brand = brand_id)
    serializer = CarSerializer(car_brand, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def home_car(request):
 
    car = Car.objects.filter(is_accepted='accepted')[:8]
    print(car)
    serializer1 = CarSerializer(car, many = True)
    return Response(serializer1.data)
        
    
    

@api_view(['GET'])
def user_list(request):
    user =  User.objects.all().order_by('id')
    serializer = UserSerializer(user, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def car_list(request):
    car = Car.objects.filter(is_accepted ='accepted')
    serializer = CarSerializer(car, many = True)
    return Response(serializer.data)
    

@api_view(['PATCH'])
def block_user(request, id):
    print('blk')
    user = User.objects.get(id = id)
    if user.is_blocked is True:
        print('unblock')
        user.is_blocked = False
        user.save()
        return Response({'status':'unblock'})
    
    else:
        print('block')
        user.is_blocked = True
        user.save()
        return Response({'status':'block'})


@api_view(['POST'])
def add_car(request):
    c = request.data['category']
    category = Category.objects.get(id=c)
    b = request.data['brand']
    brand = Brand.objects.get(id=b) 
    name = request.data['name']
    fuel_type = request.data['fuel_type']
    ac = request.data['ac']
    print(ac)
    rent_price = request.data['rent_price']
    print(rent_price,'///////')
    image =request.data['image']
    description = request.data['description']
    image1 =request.data['image1']
    image2 = request.data['image2']
    image3= request.data['image3']
    car = Car.objects.create(
                             category = category,
                             brand=brand,
                             name=name,
                             fuel=fuel_type,
                             ac=ac,
                             rent_price=rent_price,
                             description=description,
                             image =image,
                             image1 = image1,
                             image2 = image2,
                             image3 = image3,
                             is_accepted='accepted'
                             )
    car.save()
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many = True)
    return Response({'status':'true','ser':serializer.data})



@api_view(['PUT'])
def edit_car(request, id):
    car = Car.objects.get(id =id)
    c = request.data['category']
    category = Category.objects.get(id=c)
    b = request.data['brand']
    brand = Brand.objects.get(id=b)
    name = request.data['name']
    fuel = request.data['fuel']
    rent_price = request.data['rent_price']
    description = request.data['description']
    image = request.data['image']
    image1 = request.data['image1']
    image2 = request.data['image2']
    image3 = request.data['image3']

    car.category = category
    car.brand = brand
    car.name = name
    car.fuel = fuel
    car.rent_price = rent_price
    car.description = description
    car.image = image
    car.image1 = image1
    car.image2 = image2
    car.image3 = image3
    car.save()
    return Response({'status':'updated Successfully'})

@api_view(['DELETE'])
def delete_Car(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return Response({'status':'Deleted Successfully'})

    

@api_view(['POST'])
def add_location(request):
    location = request.data['location']
    car_id = request.data['car']
    car = Car.objects.get(id=car_id)
    car.location=location
    car.save()
    return Response({'status':'Location Added'})

@api_view(['GET'])
def get_location(request):
    location = Car.objects.exclude(location__isnull = True).values('location').distinct()
    serializer = LocationSerilaizer(location , many = True)
    return Response(serializer.data)
 

@api_view(['GET'])
def get_car_names(request):
    car = Car.objects.values('id','name')
    serializer = CarNameSerializer(car, many = True)
    return Response (serializer.data) 


@api_view(['POST'])
def add_Category(request):
    category = request.data['title']
    cat = Category.objects.create(title = category)
    cat.save()
    return Response({'status':'Category Added'})


@api_view(['POST'])
def add_brand(request):
    c = request.data['category']
    category = Category.objects.get(title = c)
    title = request.data['title']
    brand = Brand.objects.create(Category_id = category.id,
                                 title = title)
    
    brand.save()
    return Response({'status':'brand added'})



@api_view(['GET'])
def get_request(request):
    rent_request = Car.objects.filter(is_accepted = 'verifying')
    if rent_request:
        renter_ids = [c.renter_id for c in rent_request]
        print(renter_ids[0])
        renter_id = Renters.objects.get(id = renter_ids[0])
        renter_name = renter_id.name
        print(renter_name)
    else:
        renter_name = None
    serializer1 = CarSerializer(rent_request, many = True)
    return Response({'ser1':serializer1.data,'ser2':renter_name})

    
@api_view(['PATCH'])
def accept_request(request, id):
    req = Car.objects.filter(id = id)
    req.update(is_accepted = 'accepted')
    return Response({'status':'Accepted'})


@api_view(['PATCH'])
def reject_request(request, id):
    req = Car.objects.filter(id = id)
    req.update(is_accepted = 'rejected')
    return Response({'status':'rejected'})
    
   
@api_view(['GET'])
def get_car_request_details(request,id):
    car = Car.objects.get(id=id)
    cat = car.category.title
    brand = car.brand.title
    serializer1 = CarSerializer(car, many=False)
    return Response({'ser1':serializer1.data,'brand':brand,'cat':cat})


@api_view(['GET'])
def get_revenue(request):
    revenue = Booking.objects.filter(status='paid')
    total = 0
    for c in revenue:
        total += c.total_rent


    return Response({'total':total})

@api_view(['GET'])
def get_dashboard(request):
    user_count = User.objects.filter(is_blocked = False).count()
    renter_count = Renters.objects.all().count()

    today = datetime.datetime.now()
    dates = (Booking.objects.filter(is_created__month = today.month)
             .values('is_created__date')
             .annotate(items=Count('id'))
             .order_by('is_created__date')
             )


    paid = (Booking.objects.filter(is_created__month = today.month)
            .values('is_created__date')
            .annotate(paid = Count('id',filter = Q(status = 'paid')))
            .order_by('is_created__date')
            )
    
    cancelled = (Booking.objects.filter(is_created__month = today.month)
                 .values('is_created__date')
                 .annotate(cancelled=Count('id',filter=Q(status = 'cancelled')))
                 .order_by('is_updated__date')
                 )
    
    print(dates,'dates')
    print(paid,'paid')
    print(cancelled,'cance')

    return Response({'dates':dates,'paid':paid,'cancelled':cancelled, 'user_count':user_count,'renter_count':renter_count})
