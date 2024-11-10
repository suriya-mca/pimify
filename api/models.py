import secrets
import string
import time
from django.db import models
from django.core.exceptions import ValidationError
from fastnanoid import generate


class NanoIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 21) 
        kwargs['default'] = lambda: generate(size=21)  
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
        return self.code


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
        return self.sku                 


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
        return self.name             


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
        return self.name             


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
    id = models.AutoField(primary_key=True)
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
        return self.name


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


def generate_secure_api_key(prefix='sk', size=32):
    """
    Generates a highly secure API key combining NanoID with additional entropy
    Format: prefix_timestamp_nanoid_entropy
    """
    # Generate timestamp hex for uniqueness
    timestamp = hex(int(time.time()))[2:]
    
    # Generate NanoID component
    nano_component = generate(size=16)
    
    # Generate additional entropy using secrets
    entropy_chars = string.ascii_letters + string.digits + '_-#@^!'
    entropy = ''.join(secrets.choice(entropy_chars) for _ in range(16))
    
    # Combine all components
    key = f"{prefix}_{timestamp}_{nano_component}_{entropy}"
    return key

class APIKey(models.Model):
    id = models.AutoField(primary_key=True)
    api_key = models.CharField(max_length=100, unique=True, editable=False,)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'API Keys'
        verbose_name_plural = 'API Keys'
        indexes = [
            models.Index(fields=['api_key'])
        ]
    
    def save(self, *args, **kwargs):
        if not self.api_key:
            while True:
                generated_key = generate_secure_api_key()
                if not APIKey.objects.filter(api_key=generated_key).exists():
                    self.api_key = generated_key
                    break
        super().save(*args, **kwargs)

    def clean(self):
        if not self.name:
            raise ValidationError({'name': 'Name is required'})

    def __str__(self):
        return f"{self.name} - {self.api_key[:12]}..."

    @classmethod
    def create_key(cls, name):
        """
        Helper method to create a new API key
        """
        api_key = cls(name=name)
        api_key.full_clean()
        api_key.save()
        return api_key


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    founded_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    api_keys = models.ForeignKey(APIKey, on_delete=models.CASCADE, related_name='organization', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Organization Details'
        verbose_name_plural = 'Organization Details'
        
    def __str__(self):
        return self.id
