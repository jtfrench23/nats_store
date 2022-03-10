from django import forms
from django.forms import ModelForm
from .models import Product

#Create product form
class ProductForm(forms.Form):
    name = forms.CharField()
    slug = forms.SlugField()
    description = forms.CharField()
    product_type= forms.CharField()
    price = forms.DecimalField()
    size = forms.CharField()
    stock = forms.IntegerField()
    product_image = forms.ImageField()
