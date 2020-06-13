from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "WebAppProject/home.html")

def information(request):
    return render(request, "WebAppProject/information.html")

def blog(request):
    return render(request, "WebAppProject/blog.html")

def aboutus(request):
    return render(request, "WebAppProject/aboutus.html")

def contactus(request):
    return render(request, "WebAppProject/contactus.html")


    
