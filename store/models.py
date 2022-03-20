from email.policy import default
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    product_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=10, null=True)
    stock = models.IntegerField()
    product_image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class CustomerManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['name']="First name must be at least 2 characters"
        if len(postData['last_name'])<2:
            errors['last_name']="Last name must be at least 2 characters"
        if len(postData['password'])<6:
            errors['password']="Password must have at least 6 characters"
        if not any(char.isupper() for char in postData['password']) and any(char.islower() for char in postData['password']):
            errors['password2']="Password must have at least one capital and one lowercase letter"
        if postData['password']!= postData['password_confirm']:
            errors['confirm_password']="passwords don't match"
        return errors    
class Customer(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    birth_date = models.DateField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomerManager()



class Owner(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Order (models.Model):
    PAYMENT_CHOICES = [
        ('P', 'pending'),
        ('C', 'Complete'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default='P')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    shipped = models.BooleanField(default=False)
class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zipcode = models.IntegerField(null=True)

