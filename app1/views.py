from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_app1(request):
    return HttpResponse('<h1>This is first function in APP1</h1>')

def second_app1(request):
    return HttpResponse('<h1><marquee>This is second function in APP1</marquee></h1>')