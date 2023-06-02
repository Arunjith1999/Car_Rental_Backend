
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.user_signup,name = 'usersignup'),
    path('userlogin/',views.user_login,name ='userlogin'),
    path('forget_password/',views.forget_password,name='forget_password'),
    path('user_profile/<int:id>/',views.user_profile,name='user_profile'),
    path('user_address/<int:id>/',views.user_address,name='user_address'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('add_profile_pic/<int:id>/',views.add_profile_pic,name='add_profile_pic'),
    path('add_id_proof/<int:id>/',views.add_id_proof,name='add_id_proof'),
    path('add_license/<int:id>/',views.add_license,name='add_license'),
    path('booking_details/',views.booking_details,name ='booking_details'),
    path('confirm_booking/',views.confirm_booking,name='confirm_booking'),
    path('get_booking_history/<int:id>/',views.get_booking_history,name='get_booking_history'),
    path('get_booked_dates/<int:id>/', views.get_booked_dates, name='get_booked_dates'),
    path('cancel_payment/',views.cancel_payment,name='cancel_payment'),
    path('profile_status/<int:id>/',views.profile_status,name='profile_status'),
    path('wallet_balance/<int:id>/',views.wallet_balance,name='wallet_balance'),
    path('add_address/<int:id>/',views.add_address,name='add_address'),
]
