from .models import *
from superuser.models import *
from rest_framework import serializers



class RenterCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    car_name = serializers.SerializerMethodField()

    def get_car_name(self, obj):
        return obj.car.name

    class Meta:
        model = Booking
        fields = ['id', 'car_name','user_id', 'start_date', 'end_date', 'total_rent', 'transaction_id', 'payment_method','status','withdrawal_status']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renter_Wallet
        fields ='__all__'
        