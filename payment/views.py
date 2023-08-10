from django.shortcuts import render
from .models import Coupon
from django.db.models import Sum,F

# Create your views here.

def checkout(request):
    basketlist=request.user.customer.basketlist.all().annotate(total_price=F('count')*F('product__price'))
    all_price = basketlist.aggregate(all_price=Sum('total_price'))['all_price'] or 0
    shipping_price = all_price * 0.07
    final_price = all_price + shipping_price
    coupon_code = request.GET.get('coupon')
    coupon_status = None    
    coupon_discount = 0
    coupon_discount_amount = 0
    if coupon_code:
        coupon = Coupon.objects.filter(code=coupon_code).first()
        if coupon:
            is_valid,message = coupon.is_valid(request.user.customer)
            if is_valid:
                coupon_status = 'valid'
                coupon_discount = coupon.discount
                coupon_discount_amount = final_price * coupon_discount / 100
                final_price -= coupon_discount_amount
            else:
                coupon_status = 'invalid'
        else:
            coupon_status = 'invalid'
    return render(request,'checkout.html')