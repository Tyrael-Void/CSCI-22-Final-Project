from django.db import models

# Create your models here.
# CUSTOMER MODELS
class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f'''CUSTOMER #: {self.id}: 
NAME: {self.firstname} {self.lastname} 
ADDRESS: {self.address} 
CITY: {self.city}'''
    
    def get_customer_initials(self):
        return self.firstname[0] + self.lastname[0]
# FOOD MODELS
class Food(models.Model):
    name =  models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_food_shortname(self):
        return self.name[0:3]

    def __str__(self):
        return f'''FOOD #:{self.id}
NAME: {self.name}
DESCRIPTION: {self.description}
PRICE: {self.price}'''
    

    
# ORDER MODELS
class Order(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('CH', 'Cash'),
        ('CD', 'Card'),
        ('DW', 'Digital Wallet')
    ]
    orderDateTime = models.DateTimeField(auto_now_add=True)
    paymentMode = models.CharField(max_length=2, choices=PAYMENT_MODE_CHOICES) #CH, CD, DW
    quantity = models.IntegerField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        total_bill = self.calculate_total_bill()
        return f'''ORDER #:{self.id}
CUSTOMER NAME | PRIMARY KEY: {self.customers.firstname} {self.customers.lastname} | {self.customers.pk}
FOOD NAME: {self.food.name}
FOOD QUANTITY: {self.quantity}
PAYMENT MODE: {self.paymentMode}
ORDER DATE AND TIME: {self.orderDateTime}
TOTAL BILL: {total_bill}'''


    def calculate_total_bill(self):
        return self.quantity * self.food.price