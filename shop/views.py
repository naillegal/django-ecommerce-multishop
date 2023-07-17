from django.shortcuts import render
from .models import Campaign,Category,Product
from django.db.models import Count
# Create your views here.


def home(request):
    slide_campaigns=Campaign.objects.filter(is_slider=True)[:3]
    nonslide_campaigns=Campaign.objects.filter(is_slider=False)[:4]
    categories=Category.objects.annotate(product_count=Count('products'))
    return render(request,'home.html',{
        "slide_campaigns": slide_campaigns,
        "nonslide_campaigns": nonslide_campaigns,
        "categories": categories,
    })

def product_list(request):
    return render(request, 'product-list.html')

def product_detail(request):
    return render(request, 'product-detail.html')
