from django.urls import path
from .views import homePageView
from .views import sayHi

urlpatterns = [
    path('', homePageView, name='home'),
    path('hi', sayHi, name='hi'),

]