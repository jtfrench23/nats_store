
from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Owner
from .forms import ProductForm, EditForm
from django.http import HttpResponseRedirect
import bcrypt

def index(request):
    context={
        'all_products': Product.objects.all()
    }
    return render(request, 'index.html', context)


def owner_login(request):
    return render(request, 'owner.html')


def register_owner(request):    
    # include some logic to validate user input before adding them to the database!
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
    print(pw_hash,"$$$$$$$$$$$$$$$$$$$$")      # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
    # be sure you set up your database so it can store password hashes this long (60 characters)
    # make sure you put the hashed password in the database, not the one from the form!
    Owner.objects.create(email=request.POST['email'], password=pw_hash) 
    user = Owner.objects.filter(email=request.POST['email'])
    if user: # note that we take advantage of truthiness here: an empty list will return false
        logged_user = user[0] 
        request.session['owner_id'] = logged_user.id
    return redirect("/product_manager") # never render on a post, always redirect!  


def validate_owner_login(request):
    user = Owner.objects.filter(email=request.POST['email']) # why are we using filter here instead of get?
    if user: # note that we take advantage of truthiness here: an empty list will return false
        logged_user = user[0] 
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['owner_id'] = logged_user.id
            # never render on a post, always redirect!
            return redirect('/product_manager')
    # if we didn't find anything in the database by searching by username or if the passwords don't match, 
    # redirect back to a safe route
    return redirect("/owner")


def add_product(request):
    if 'owner_id' not in request.session:
        return redirect('/owner')
    else:
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
    if 'owner_id' not in request.session:
        return redirect('/owner')
    else:
        context={
            'all_products': Product.objects.all()
        }
        return render(request, 'product_manager.html', context)


def edit_product(request, id):
    if 'owner_id' not in request.session:
        return redirect('/owner')
    else:
        context={'product':Product.objects.get(id=id)}
        if request.method=="POST":
            form = EditForm(request.POST)
            if form.is_valid():
                p=Product.objects.get(id=id)
                name = request.POST['name']
                slug = request.POST['slug']
                description=request.POST['description']
                product_type=request.POST['product_type']
                price=request.POST['price']
                size=request.POST['size']
                stock=request.POST['stock']
                p.name=name
                p.slug=slug
                p.description=description
                p.product_type=product_type
                p.price=price
                p.size=size
                p.stock=stock
                p.save()
                return redirect('/product_manager')
        else:
            p=p=Product.objects.get(id=id)
            data_dict={'name': p.name, 'slug': p.slug, 'description':p.description, 'product_type': p.product_type, 'price':p.price, 'size':p.size, 'stock':p.stock}
            form = EditForm(data_dict)
        context['form']= form
        return render(request, "product_edit.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')
def delete_product(request, id):
    p=Product.objects.get(id=id)
    p.delete()
    return redirect('/product_manager')
