#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHi(request):
    return HttpResponse('<h1>Hai buddy<h1>')
    
def homePageView(request):
    return HttpResponse('Hello world!')

