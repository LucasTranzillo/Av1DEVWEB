from django.shortcuts import render
from stweb.models import Product

# Create your views here.

def index(request) :
    productList = Product.objects.all()
    context = {
        'products' : productList
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def store(request):
    return render(request, 'store.html')

def service(request):
    return render(request, 'service.html')