from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): # django request parameters
    return HttpResponse("<h1> Hey, I am a django server.</h1>")


def success_page(request):
    print("kishan namdev")
    return HttpResponse("<h2> Hey this is a success page</h2>")