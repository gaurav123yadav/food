from django.urls import path 
from . import views
urlpatterns=[
    path("",views.home ,name='home'),
    path("about",views.about ,name='about'),
    path("privacy",views.privacy ,name='privacy'),
    path("terms&conditions",views.terms,name='terms&conditions'),
    path("contact",views.contact,name='contact'),
    path("shop",views.shop,name='shop'),
    path("login",views.login,name='login'),
    path("register",views.register,name='register'),
    path("checkout",views.order,name='order'),
    path("cart",views.cart,name='cart'),
    path("forgot-password",views.forgot,name='forgot-password'),
    path("reset-password",views.reset,name='reset-password'),
    path("logout",views.logout,name='logout'),
    path("search",views.search,name='search'),
    path("add-to-cart",views.addToCart,name='addToCart'),
    path("remove-from-cart",views.removeFromCart,name='removeFromCart'),
    path("order-success/<orderId>",views.orderAccept,name='orderSuccess'),
    path("my-orders",views.myOrders,name='myOrders'),
]
