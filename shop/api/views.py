from django.http import JsonResponse
from ..models import Product
from customer.models import WishItem

def add_wish(request, pk):
    WishItem.objects.create(customer=request.user.customer,product_id=pk)
    return JsonResponse({'result':'added'})


def remove_wish(request, pk):
    WishItem.objects.filter(customer=request.user.customer,product_id=pk).delete()
    return JsonResponse({'result':'removed'})
    