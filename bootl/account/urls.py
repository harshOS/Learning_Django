from django.urls import path
from .views import Homepage, Contactpage

urlpatterns =[
    path('',Homepage.as_view(),name = 'home')
    path('contact',Homepage.as_view(),name = 'contact')

]