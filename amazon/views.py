from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil

def index(request):
    products= product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"amazon/index.html", params)
    
    #  return render(request, 'amazon/index.html')


def about(request):
    return render(request, 'amazon/about.html')
def contact(request):
    return HttpResponse("contact")
def search(request):
    return HttpResponse("search")
def productview(request):
    return HttpResponse("productview")
def checkout(request):
    return HttpResponse("checkout")
def tracker(request):
    return HttpResponse("tracker")
