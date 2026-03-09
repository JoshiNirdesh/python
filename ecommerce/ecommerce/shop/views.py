from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
# Create your views here.
def index(request):
    product = Product.objects.all()
    print(product)
    params = {"product":product}
    return render(request,'shop/index.html',params)

def about(request):
    return HttpResponse("About us page")

def contact(request):
    return HttpResponse("Contact")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")

def productview(request):
    return HttpResponse("product view")

def checkout(request):
    return HttpResponse("checkout")
