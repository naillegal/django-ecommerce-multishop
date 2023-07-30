from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Campaign,Category,Product
from django.db.models import Count
from customer.models import Review
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

def product_detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
    current_review=None
    if (request.user.is_authenticated and request.user.customer):
        current_review=has_review=Review.objects.filter(customer=request.user.customer,product=product).first()
    return render(request,'product-detail.html',{'product':product,'current_review':current_review})


def review(request,pk):
    if request.method == 'POST':
        customer=request.user.customer
        product = get_object_or_404(Product, pk=pk)
        if Review.objects.filter(customer=customer , product=product).exists():
            return HttpResponse(status=403)
        star_count = int(request.POST.get('star_count'))
        comment = request.POST.get('comment')
        Review.objects.create(
            customer=customer,
            product=product,
            star_count=star_count,
            comment=comment
        )
        return redirect('shop:product-detail', pk=pk)
    return redirect('shop:product-detail', pk=pk)
    
                         