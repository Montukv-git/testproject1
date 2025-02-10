from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def home(request):
    data = {
        'name': request.GET['name']
    }
    return render(request, 'home.html', data)