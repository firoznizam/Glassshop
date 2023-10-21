from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def productsview(request):
    return render(request,'products.html')

def aboutview(request):
    return render(request,'about.html')

def blogsview(request):
    return render(request,'blogs.html')

def contactview(request):
    return render(request,'contact.html')

def loginview(request):
    return render(request,'login.html')

def registerview(request):
    return render(request,'register.html')

# Create your views here.

# Create your views here.
