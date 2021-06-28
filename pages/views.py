from os import error
from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import *
import json

passwordSalt="guu khaa tu madam maira"

# Create your views here.
def home(request):
    products = product.getAllProducts(limit=8)
    bestSellerProducts = product.getBestSeller()
    ctx = {}
    ctx['products'] = products
    ctx['bestSellerProducts'] = bestSellerProducts
    return render(request,'home.html', ctx)

def about(request):
    return render(request,'about.html')

def privacy(request):
    return render(request,'privacy.html')

def terms(request):
    return render(request,'terms&conditions.html')    

def contact(request):
    return render(request,'contact.html')   

def shop(request):
    products = None
    ctx = {}
    categories = Category.getAllCategories()
    categoryId = request.GET.get('category')
    if categoryId:
        ctx['categoryId'] = int(categoryId)
        products = product.getAllProductsByCategoryId(categoryId)
    else:
        products = product.getAllProducts()
    
    ctx['products'] = products
    ctx['categories'] = categories
    return render(request,'shop.html', ctx)      

def search(request):
    products = None
    ctx = {}
    try:
        products =product.objects.filter(name__contains=request.GET.get('q'))
        ctx['products'] = products
    except:
        ctx['products'] = []
    return render(request,'search.html', ctx)      


def cart(request):
    cartItems = Cart.objects.all()
    totalAmount = 0
    for item in cartItems:
        totalAmount += item.product_id.price * item.quantity

    ctx ={}
    ctx['cartItems'] = cartItems
    ctx['totalAmount'] = totalAmount
    return render(request,'cart.html', ctx)

def reset(request):
    return render(request,'reset-password.html')

def forgot(request):
    return render(request,'forgot-password.html')

def order(request):
    cartItems = Cart.objects.all()
    totalAmount = 0
    for item in cartItems:
        totalAmount += item.product_id.price * item.quantity

    ctx ={}
    ctx['cartItems'] = cartItems
    ctx['totalAmount'] = totalAmount
    if(request.method == 'POST'):
        user = request.session['user']
        order = Order(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            billing_address = request.POST.get('billing_address'),
            country = request.POST.get('country'),
            city = request.POST.get('city'),
            amount= totalAmount, 
            user_id = User.objects.get(id=user.get('id')) 
            )
        order.save()

        for item in cartItems:
            orderItems = Order_items(
                product_id = item.product_id,
                quantity = item.quantity,
                order_id = order
            )
            orderItems.save()
            
        Cart.objects.all().delete()
        return redirect('orderSuccess', orderId = order.id)
    return render(request,'order.html',ctx)

def orderAccept(request, orderId):
    ctx={}
    try:
        order = Order.objects.get(id=orderId)
        orderItems= Order_items.objects.filter(order_id=order)
        ctx['order'] = order
        ctx['orderItems'] = orderItems
    except:
        ctx['order'] = None
        ctx['orderItems']= []
    return render(request,'success.html', ctx)

def myOrders(request):
    ctx={}
    try:
        user = User.objects.get(id=request.session['user'].get('id'))
        ctx['orders'] = Order.objects.filter(user_id=user)
    except:
        ctx['orders']=[]
    return render(request, 'my-order.html', ctx)
    
def register(request):
    context = {}
    
    formData = request.POST
   
    
    if(request.method == "POST"):
        formData.email = request.POST.get('email')
        formData.password = make_password(request.POST.get('password'), passwordSalt)
        user = User(email=formData.email, password = formData.password)
        if(user.save()):
            request.session['authenticated'] = True
            request.session['user'] = {
                "id": user.id,
                "email": user.email
            }
            
            return redirect('home')
    
   
    return render(request,'register.html', context)


def login(request):
    try:
        if(request.method == "POST"):
            formData = request.POST
            formData.email = request.POST.get('email')
            formData.password = make_password(request.POST.get('password'), passwordSalt)
            
            user = User.objects.get(email = formData.email,password = formData.password)
            if(user):
                request.session['authenticated'] = True
                request.session['user'] = {
                    "id": user.id,
                    "email": user.email
                }
                
                return redirect('home')
    except:
        user =None
    return render(request,'login.html')

def logout(request):
    request.session['auntenticated'] = False
    request.session.flush()
    return redirect('home')

def addToCart(request):
    if(request.method == "POST"):
        try:
            product_id = request.POST.get('product_id')
            quantity = request.POST.get('quantity')
            prod = product.objects.get(id=product_id)
            products = Cart.objects.filter(product_id=prod)
            if(products and len(products) > 0):
                cartObj = Cart.objects.get(product_id = product_id)
                cartObj.quantity = quantity
                cartObj.save()
            else:
                cartObj = Cart(product_id=prod, quantity=quantity)
                cartObj.save()
            return HttpResponse(True) 
        except:
            return HttpResponse(False)

def removeFromCart(request):
    try:
        productId = request.POST.get('product_id')
        prod = product.objects.get(id=productId)
        Cart.objects.filter(product_id=prod).delete()
        return HttpResponse(True)
    except:
        return HttpResponse(False)
