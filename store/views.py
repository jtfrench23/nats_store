
from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseRedirect

def index(request):
    context={
        'all_products': Product.objects.all()
    }
    return render(request, 'index.html', context)
def add_image(request):
    Product.objects.create(request.POST, request.FILES)
    return redirect('/')
def add_product(request):
    context ={}
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            slug = form.cleaned_data.get('slug')
            description=form.cleaned_data.get('description')
            product_type=form.cleaned_data.get('product_type')
            price=form.cleaned_data.get('price')
            size=form.cleaned_data.get('size')
            stock=form.cleaned_data.get('stock')
            product_image = form.cleaned_data.get("product_image")
            obj = Product.objects.create(
                                name = name,
                                slug = slug,
                                description = description,
                                product_type=product_type,
                                price=price,
                                size=size,
                                stock=stock,
                                product_image = product_image
                                )
            obj.save()
            print(obj)
    else:
        form = ProductForm()
    context['form']= form
    return render(request, "add_product.html", context)
def product_manager(request):
    context={
        'all_products': Product.objects.all()
    }
    return render(request, 'product_manager.html', context)
def edit_product(request, id):
    context={'product':Product.objects.get(id=id)}
    return render(request, 'product_edit.html', context)
def delete_product(request, id):
    p=Product.objects.get(id=id)
    p.delete()
    return redirect('/product_manager')