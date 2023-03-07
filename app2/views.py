from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_app2(request):
    return HttpResponse('<h1>This is first function in APP2</h2>')

def second_app2(request):
    return HttpResponse('<h1><button>This is second function in APP2<button></h2>')    