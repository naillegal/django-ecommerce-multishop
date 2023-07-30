from django import template
from ..models import GeneralCategory,Category
from customer.models import WishItem


register=template.Library()

@register.inclusion_tag('includes/nav-categories.html')

def nav_category():
    pure_categories=Category.objects.filter(general_category__isnull=True)
    general_categories=GeneralCategory.objects.all()
    return {
        'pure_categories':pure_categories,
        'general_categories':general_categories,
    }

@register.inclusion_tag('includes/star.html')

def star(star_count):
    full_star=int(star_count)
    half_star=full_star!=star_count
    empty_star=5-(full_star+int(half_star))
    return {
        'full_star':range(full_star),
        'half_star':half_star,
        'empty_star':range(empty_star),
    }

@register.filter
def is_wished(product,request):
    if not request.user.is_authenticated:
        return False
    
    return WishItem.objects.filter(product=product,customer=request.user.customer).exists()

