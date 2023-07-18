from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Food, Customer, Order
from .forms import FoodForm, CustomerForm, OrderForm
from django.contrib.auth import authenticate, login



# Create your views here.

def index(request):
    #body = '''<h1>bITEbox - WebKiosk</h1>
    #<p>Yum Yum Yummy</p>
    #<h2>Welcome</h2>
    #<p>Welcome to the bITEbox Webkiosk where you can manage the menu, orders and customers.</p>'''
    #return HttpResponse(body)
    return render(request, 'webkiosk/welcom.html')

def testview(request):
    return render(request, 'webkiosk/testpage.html')


def listfood(request):
    fl = Food.objects.all()
    context = {'foodlist': fl}
    return render(request, 'webkiosk/food_list.html', context)


def createfood(request):
    if request.method == "GET":
        f = FoodForm()
    elif request.method == 'POST':
        f = FoodForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('webkiosk:food-list')

    f = FoodForm
    context = { 'form': f, 'formheading': 'Add Food' }
    return render(request, 'webkiosk/food_form.html', context)


def detailfood(request, pk):
    f = Food.objects.get(id=pk)
    context = {'food': f}
    return render(request, 'webkiosk/food_detail.html', context )


def updatefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        form = FoodForm(instance=food)
    elif request.method == 'POST':
        form = FoodForm(request.POST,instance=food)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Food Successfully Updated!')
    context = {'form':form,'formheading':'Update Food'}
    return render(request, 'webkiosk/food_form.html', context)

     
def deletefood(request, pk):
    f = Food.objects.get(id=pk)
    if request.method == "GET":
        context = {'food': f}
        return render(request, 'webkiosk/food_delete.html', context)
    elif request.method == "POST":  
        f.delete()
        return redirect('webkiosk:food-list')

def listcustomer(request):
    cl = Customer.objects.all()
    context = {'customerlist': cl}
    return render(request, 'webkiosk/customer_list.html', context)


def addcustomer(request):
    if request.method == "GET":
        c = CustomerForm()
    elif request.method == 'POST':
        c = CustomerForm(request.POST)
        if c.is_valid():
            c.save()
            return redirect('webkiosk:customer-list')

    c = CustomerForm
    context = { 'form': c, 'formheading': 'Add Customer' }
    return render(request, 'webkiosk/customer_form.html', context)


def customerdetails(request, pk):
    c = Customer.objects.get(id=pk)
    o = Order.objects.filter(customers=c)
    context = {'customer': c, 'order': o}
    return render(request, 'webkiosk/customer_detail.html', context )


def updatecustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        form = CustomerForm(instance=customer)
    elif request.method == 'POST':
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Customer Profile Successfully Updated!')
    context = {'form':form,'formheading':'Update Customer'}
    return render(request, 'webkiosk/customer_form.html', context)


def deletecustomer(request, pk):
    c = Customer.objects.get(id=pk)
    if request.method == "GET":
        context = {'customer': c}
        return render(request, 'webkiosk/customer_delete.html', context)
    elif request.method == "POST":  
        c.delete()
        return redirect('webkiosk:customer-list')


def listorder(request):
    o = Order.objects.all()
    context = {'orderlist': o}
    return render(request, 'webkiosk/order_list.html', context)


def orderform(request):
    if request.method == "GET":
        o = OrderForm()
    elif request.method == 'POST':
        o = OrderForm(request.POST)
        if o.is_valid():
            o.save()
            return redirect('webkiosk:order-list')

    o = OrderForm
    context = { 'form': o, 'formheading': 'Place Order' }
    return render(request, 'webkiosk/order_form.html', context)


def orderdetails(request, pk):
    d = Order.objects.get(id=pk)
    context = {'order': d}
    return render(request, 'webkiosk/order_details.html', context )


def updateorder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'GET':
        form = OrderForm(instance=order)
    elif request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Order Successfully Updated!')
    context = {'form':form,'formheading':'Update Order'}
    return render(request, 'webkiosk/order_form.html', context)


def deleteorder(request, pk):
    o = Order.objects.get(id=pk)
    if request.method == "GET":
        context = {'order': o}
        return render(request, 'webkiosk/order_delete.html', context)
    elif request.method == "POST":  
        o.delete()
        return redirect('webkiosk:order-list')
    



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webkiosk:food-list')  # Redirect to the home page after successful login
        else:
            error = 'Invalid credentials'
            return render(request, 'webkiosk/login.html', {'error': error})

    return render(request, 'webkiosk/login.html')