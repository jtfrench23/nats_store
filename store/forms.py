from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import Product

#Create product form
class ProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={'placeholder': 'slug', 'style': 'width: 300px;', 'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'style': 'width: 300px;'}))
    product_type= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'type', 'style': 'width: 300px;', 'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '1.99', 'style': 'width: 300px;', 'class': 'form-control'}))
    size = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'size', 'style': 'width: 300px;', 'class': 'form-control'}))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '1', 'style': 'width: 300px;', 'class': 'form-control'}))
    product_image = forms.ImageField()
class EditForm(forms.Form):
    name = forms.CharField()
    slug = forms.SlugField()
    description = forms.CharField(widget=forms.Textarea)
    product_type= forms.CharField()
    price = forms.DecimalField()
    size = forms.CharField()
    stock = forms.IntegerField()
class CustomerForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 200px;', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 200px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 200px;', 'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '123-456-7890', 'style': 'width: 200px;', 'class': 'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 200px;', 'class': 'form-control'}))
    password_confirm=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 200px;', 'class': 'form-control'}))
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 200px;', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 200px;', 'class': 'form-control'}))