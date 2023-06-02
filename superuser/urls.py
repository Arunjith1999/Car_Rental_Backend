from .import views
from django.urls import path

urlpatterns = [
    path('admin/',views.admin_login,name='admin'),
    path('category/',views.Get_Category,name='category'),
    path('brand/',views.brand,name='brand'),
    path('brands/<int:id>/',views.brands,name='brands'),
    path('car_models/<int:id>/', views.car_models,name='car_models'),
    path('car_brand/<int:id>/<int:brand_id>/',views.car_brands,name='car_brand'),
    path('home_car/',views.home_car,name='home_car'),
    path('car_details/<int:id>/',views.car_details,name='car_details'),
    path('user_list/',views.user_list,name='user_list'),
    path('car_list/',views.car_list, name='car_list'),
    path('block_user/<int:id>',views.block_user, name='block_user'),
    path('add_car/',views.add_car,name='add_car'),
    path('edit_car/<int:id>/',views.edit_car,name='edit_car'),
    path('delete_car/<int:id>/',views.delete_Car,name = 'delete_car'),
    path('add_location/',views.add_location,name='add_location'),
    path('get_location/',views.get_location,name = 'get_location'),
    path('get_car_names/',views.get_car_names,name='get_car_names'),
    path('add_Category/',views.add_Category,name='add_Category'),
    path('add_brand/',views.add_brand,name ='add_brand'),
    path('get_request/',views.get_request,name='get_request'),
    path('accept_request/<int:id>/',views.accept_request,name='accept_request'),
    path('reject_request/<int:id>/',views.reject_request,name='reject_request'),
    path('get_car_request_details/<int:id>/',views.get_car_request_details,name='get_car_request_details'),
    path('get_revenue/',views.get_revenue,name='get_revenue'),
    path('get_dashboard/',views.get_dashboard,name='get_dashboard'),

]
