from django.shortcuts import render, redirect,get_object_or_404
from .forms import ContactForm, RegisterForm
from django.contrib.auth import login,logout,authenticate
from .models import WishItem
from django.contrib.auth.decorators import login_required
from shop.models import Product



# Create your views here.


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm, 'result': 'success'})
        return render(request, 'contact.html', {'form': form, 'result': 'fail'})
    return render(request, 'contact.html', {'form': form})


def wishlist(request):
    return render(request, 'wishlist.html')

@login_required
def wish_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    customer=request.user.customer
    wishitem=WishItem.objects.filter(product=product, customer=customer).delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def unwish_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    customer=request.user.customer
    wishitem=WishItem.objects.create(product=product, customer=customer)
    return redirect(request.META.get('HTTP_REFERER'))


def basket(request):
    return render(request, 'basket.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        if remember_me:
            request.session.set_expiry(1209600)
        else:
            request.session.set_expiry(0)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('shop:home')
        else:
            return render(request, 'login.html', context={'unsuccessful': True})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('shop:home')
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('customer:login')