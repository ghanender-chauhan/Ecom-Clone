from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello Genius")
def about(request):
    return HttpResponse("Its Ecom About")