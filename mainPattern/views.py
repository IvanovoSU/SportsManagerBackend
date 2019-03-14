from django.shortcuts import render

def index(request):
    return render(request, 'mainPattern/home.html')

def login(request):
    return render(request, 'mainPattern/login.html')
