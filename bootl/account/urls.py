from django.urls import path
from .views import Products, HomePage

urlpatterns =[
    path('', HomePage, name = 'home'),
    path('contact', Products, name = 'Products'),

]