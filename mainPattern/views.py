from django.shortcuts import render

def index(request):
    years = range(1902, 2006);
    months = range(1, 13);
    days = range(1, 32,)
    return render(request, 'mainPattern/home.html', {'years': years, 'months' : months, 'days': days,})

def login(request):
    return render(request, 'mainPattern/login.html')
