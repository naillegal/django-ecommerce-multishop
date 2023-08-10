from django.db import models
from django.utils import timezone

# Create your models here.

class Coupon(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    discount = models.FloatField()
    used_customers = models.ManyToManyField('customer.Customer',related_name='used_coupons',blank=True)
    expire = models.DateTimeField()
    limit = models.IntegerField(null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    def is_valid(self,customer):
        if timezone.localtime() > self.expire:
            return (False,'Bu kuponun istifade tarixi bitmisdir')
        elif self.used_customers.count() >= self.limit:
            return (False,'Bu kuponun istifade limiti bitmisdir')
        elif self.used_customers.contains(customer):
            return (False,'Siz artiq bu kuponu istifade etmisiniz')
        else:
            return [True,'Kupon ugurla istifade olundu']
        

COUNTRIES = [
    ('azerbaijan','Azerbaijan'),
    ('russia','Russia'),
    ('turkey','Turkey'),
    ('usa','USA'),
]



class Order(models.Model):
    customer = models.ForeignKey('customer.Customer',on_delete=models.SET_NULL,null=True)
    used_coupon = models.ForeignKey(Coupon, null=True ,blank=True,on_delete=models.SET_NULL)
    accepted = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    country = models.CharField(max_length=50,choices=COUNTRIES)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    created =  models.DateTimeField(auto_now_add=True)


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='products')
    title = models.CharField(max_length=50)
    price = models.FloatField()
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

