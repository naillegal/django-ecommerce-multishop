from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        exclude = ['customer','used_coupon','accepted','delivered','created']
        model = Order
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.SelectMultiple(attrs={'class':'custom-select'})
        }