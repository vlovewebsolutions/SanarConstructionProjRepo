from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')