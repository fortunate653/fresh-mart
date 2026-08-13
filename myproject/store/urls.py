from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home,name='home'),
    path('product/', views.products,name='products'),
    path('cart/', views.cart, name='cart'),
]