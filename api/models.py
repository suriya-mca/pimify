from django.db import models
from fastnanoid import generate


class NanoIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 21) 
        kwargs['default'] = generate(size=21)  
        kwargs['editable'] = False
        super().__init__(*args, **kwargs) 


class Currency(models.Model):
    id = NanoIDField(primary_key=True)
    code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=1)

    def __str__(self):
        return self.id


class Product(models.Model):
    id = NanoIDField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)          
    stock_quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    categories = models.ManyToManyField('Category', related_name='products')      
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
        
    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
            models.Index(fields=['sku']),
        ]                   


class Category(models.Model):
    id = NanoIDField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.id
        
    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),      
        ]                 


class Supplier(models.Model):
    id = NanoIDField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.id
        
    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),          	
        ]               


class ProductSupplier(models.Model):
    id = NanoIDField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='suppliers')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    lead_time = models.IntegerField(help_text="Lead time in days")

    class Meta:
        unique_together = ('product', 'supplier')

    def __str__(self):
        return self.id


class ProductImage(models.Model):
    id = NanoIDField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.id


class Warehouse(models.Model):
    id = NanoIDField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.id
        
    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),       
        ]


class Stock(models.Model):
    id = NanoIDField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
        
    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]
