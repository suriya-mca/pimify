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

    class Meta:
        db_table = 'Currencies'
        verbose_name_plural = 'Currencies'

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

    class Meta:
        db_table = 'Products'
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),
            models.Index(fields=['sku']),
        ] 

    def __str__(self):
        return self.id                  


class Category(models.Model):
    id = NanoIDField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'Categories'
        verbose_name_plural = 'Categories'
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),      
        ]   

    def __str__(self):
        return self.id              


class Supplier(models.Model):
    id = NanoIDField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        db_table = 'Suppliers'
        verbose_name_plural = 'Suppliers'
        
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),          	
        ] 

    def __str__(self):
        return self.id              


class ProductSupplier(models.Model):
    id = NanoIDField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='suppliers')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    lead_time = models.IntegerField(help_text="Lead time in days")

    class Meta:
        db_table = 'Product Suppliers'
        verbose_name_plural = 'Product Suppliers'
        unique_together = ('product', 'supplier')

    def __str__(self):
        return self.id


class ProductImage(models.Model):
    id = NanoIDField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Product Images'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.id


class Warehouse(models.Model):
    id = NanoIDField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        db_table = 'Warehouses'
        verbose_name_plural = 'Warehouses'
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['name']),       
        ]

    def __str__(self):
        return self.id


class Stock(models.Model):
    id = NanoIDField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Stocks'
        verbose_name_plural = 'Stocks'
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.id


class Organization(models.Model):
    id = NanoIDField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    founded_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Organization Details'
        verbose_name_plural = 'Organization Details'
        
    def __str__(self):
        return self.id
