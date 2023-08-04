from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def viewer(request):
    return render(request, 'viewer.html')

def designer(request):
    return render(request, 'designer.html')