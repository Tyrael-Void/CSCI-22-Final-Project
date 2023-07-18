from django.forms import ModelForm
from .models import Food, Customer, Order

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'address', 'city']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['paymentMode', 'quantity', 'food', 'customers']