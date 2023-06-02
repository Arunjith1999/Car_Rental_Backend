from .models import *
from rest_framework import serializers



class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields ='__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'