from django.shortcuts import render

# Create your views here.


def contact(request):
    return render(request, 'contact.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def basket(request):
    return render(request, 'basket.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def logout_view(request):
    pass