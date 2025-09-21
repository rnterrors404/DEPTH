from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):    
    return render(request,"index.html")

def sign_up(request):
    return render(request, "sign_up.html")

def about_us(request):
    return render(request,"about_us.html")

def login_page(request):
    return render(request, "login_page.html")