from django.urls import path
from .import views

urlpatterns = [
    path('renter_signup/',views.renter_signup,name='renter_signup'),
    path('renter_login/',views.renter_login,name='renter_login'),
    path('request_car/<int:id>/',views.request_car,name='request_car'),
    path('get_car/<int:id>/',views.get_car,name='get_car'),
    path('get_car_request_details/<int:id>/',views.get_car_request_details,name='get_car_request_details'),
    path('get_booking_details/<int:id>/',views.get_booking_details,name= 'get_booking_details'),
    path('credit_wallet/',views.credit_wallet,name='credit_wallet'),
    path('get_balance/<int:id>/',views.get_balance,name='get_balance'),
]
