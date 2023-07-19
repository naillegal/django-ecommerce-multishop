from django.shortcuts import render
from .models import Campaign,Category,Product
from django.db.models import Count
# Create your views here.


def home(request):
    slide_campaigns=Campaign.objects.filter(is_slider=True)[:3]
    nonslide_campaigns=Campaign.objects.filter(is_slider=False)[:4]
    categories=Category.objects.annotate(product_count=Count('products'))
    featured_products=Product.objects.filter(featured=True)[:8]
    recent_products=Product.objects.all().order_by('-created')[:8]
    return render(request,'home.html',{
        "slide_campaigns": slide_campaigns,
        "nonslide_campaigns": nonslide_campaigns,
        "categories": categories,
        "featured_products": featured_products,
        "recent_products": recent_products,
    })

def product_list(request):
    return render(request, 'product-list.html')

def product_detail(request):
    return render(request, 'product-detail.html')
