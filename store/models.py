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
class Customer(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    birth_date = models.DateField(null = True)
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
    customer= models.ForeignKey(Customer, on_delete=models.PROTECT)
class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
class Cart(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
class address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zipcode = models.IntegerField(null=True)

