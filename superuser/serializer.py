from .models import *
from rest_framework import serializers
from users.models import *
from renters.models import*

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LocationSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['location']

class CarNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','name']


class RenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renters
        fields = ['id','name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Brand
        fields ='__all__'

class BookingSerializer(serializers.ModelSerializer):
    car_name = serializers.SerializerMethodField()

    def get_car_name(self, obj):
        return obj.car.name

    class Meta:
        model = Booking
        fields = ['id', 'car_name','user_id', 'start_date', 'end_date', 'total_rent', 'transaction_id', 'payment_method','status']