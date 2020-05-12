from django.urls import path
from .views import Products, HomePage

urlpatterns =[
    path('', HomePage, name = 'home'),
    path('dashboard', HomePage, name = 'dashboard'),
    path('products', Products, name = 'Products'),
    path()

]