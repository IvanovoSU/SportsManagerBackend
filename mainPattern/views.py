from django.shortcuts import render
from random import randint

def index(request):
    years = range(1902, 2006);
    months = range(1, 13);
    days = range(1, 32,)
    background = randint(1, 6);
    return render(request, 'mainPattern/home.html', {'years': years, 'months' : months, 'days': days, 'background' : background,})

def login(request):
    background = randint(1, 6);
    return render(request, 'mainPattern/login.html', {'background' : background,})
