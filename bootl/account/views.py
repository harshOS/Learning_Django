from django.shortcuts import render
from django.http import HttpResponse

def Products(request):
     return render(request, 'account/products.html')    

def HomePage(request):
    return render(request, 'account/dashboard.html')



    
     

