from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import Product

#Create product form
class ProductForm(forms.Form):
    name = forms.CharField()
    slug = forms.SlugField()
    description = forms.CharField(widget=forms.Textarea)
    product_type= forms.CharField()
    price = forms.DecimalField()
    size = forms.CharField()
    stock = forms.IntegerField()
    product_image = forms.ImageField()
class EditForm(forms.Form):
    name = forms.CharField()
    slug = forms.SlugField()
    description = forms.CharField(widget=forms.Textarea)
    product_type= forms.CharField()
    price = forms.DecimalField()
    size = forms.CharField()
    stock = forms.IntegerField()