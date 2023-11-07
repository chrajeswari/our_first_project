from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Raji(request):
    return HttpResponse('<h1><marquee>Hi Raji How Are You</h1></marquee>')
def swetha(request):
    return HttpResponse('<h1><marquee>swetha is a waste fellow</h1></marquee>')