from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name()
    

class Review(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='reviews')
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='reviews')
    comment=models.TextField()
    star_count=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created=models.DateField(auto_now_add=True)
    