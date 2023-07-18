from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'webkiosk'

urlpatterns = [
    #http://localhost:8000/webkiosk/
    path('', views.index, name='index'),

    path('testview/', views.testview, name='testview'),

    #http://localhost:8000/webkiosk/menu/
    path('menu/', views.listfood, name='food-list'),

    #http://localhost:8000/webkiosk/menu/
    path('food/new/', views.createfood, name = 'food-create'),

    #http:localhost:8000/webkiosk/food/1
    path('food/<int:pk>', views.detailfood, name='food-details'),

    #http:localhost:8000/webkiosk/food/1/edit/
    path('food/<int:pk>/edit', views.updatefood, name='food-update'),

    #http:localhost:8000/webkiosk/food/1/delete/
    path('food/<int:pk>/delete', views.deletefood, name='food-delete'),

    #http:localhost:8000/webkiosk/customers/
    path('customer/', views.listcustomer, name='customer-list'),

    #http:localhost:8000/webkiosk/customer/**pk**/
    path('customer/<int:pk>/', views.customerdetails, name='customer-details'),

    #http:localhost:8000/webkiosk/customer/new
    path('customer/new/', views.addcustomer, name = 'add-customer'),

    #http:localhost:8000/webkiosk/customer/1/edit
    path('customer/<int:pk>/edit', views.updatecustomer, name='customer-update'),

    #http:localhost:8000/webkiosk/customer/1/delete
    path('customer/<int:pk>/delete', views.deletecustomer, name='customer-delete'),

    #http:localhost:8000/webkiosk/orders
    path('orders/', views.listorder, name='order-list'),

    #http:localhost:8000/webkiosk/orders/add
    path('orders/add', views.orderform, name='order-form'),

    #http:localhost:8000/webkiosk/orders/1
    path('orders/<int:pk>', views.orderdetails, name='order-details'),

    #http:localhost:8000/webkiosk/order/1/edit
    path('orders/<int:pk>/edit', views.updateorder, name='order-update'),

    #http:localhost:8000/webkiosk/order/1/delete
    path('orders/<int:pk>/delete', views.deleteorder, name='delete-order'),
    
    #http:localhost:8000/webkiosk/login/
    path('login/', views.login_page, name='login'),

    #http:localhost:8000/webkiosk/logout/
    path('logout/', auth_views.LogoutView.as_view(next_page='webkiosk:login'), name='logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)