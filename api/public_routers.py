from ninja import Router
from typing import List, Optional
from django.shortcuts import get_object_or_404
from ninja.pagination import paginate

from .schemas import Message, ProductListSchema, ProductInfoSchema, ProductImageSchema, CategorySchema, SupplierListSchema, SupplierInfoSchema, WarehouseListSchema, WarehouseInfoSchema, StockDetailSchema
from .models import Product, ProductImage, Category, Supplier, Warehouse, Stock


router = Router()


@router.get("/health", response={200: Message, 204: None}, tags=["Product"])
def health_check(request):

    return 200, {'message': 'success'}


@router.get("/products/", response={200: List[ProductListSchema]}, tags=["Product"])
@paginate
def list_products(request, is_active: Optional[bool] = None):

    products = Product.objects.prefetch_related('currency').filter(is_active=is_active) if is_active is not None else Product.objects.all().prefetch_related('currency')
    return products


@router.get("/products/{id}/", response={200: ProductInfoSchema}, tags=["Product"])
def retrieve_product(request, id: str):

    product = get_object_or_404(Product, id=id)
    return product


@router.get("/products/{id}/images/", response={200: List[ProductImageSchema]}, tags=["Product"])
def retrieve_product_images(request, id: str):

    product = get_object_or_404(Product, id=id)
    images = ProductImage.objects.filter(product=product)
    return images


@router.get("/categories/", response={200: List[CategorySchema]}, tags=["Product"])
@paginate
def list_categories(request):

    categories = Category.objects.all()
    return categories


@router.get("/categories/{category_id}/products/", response={200: List[ProductListSchema]}, tags=["Product"])
@paginate
def list_products_by_category(request, category_id: str):
    
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(categories=category)
    return products


@router.get("/search/products/", response={200: List[ProductListSchema]}, tags=["Product"])
def search_products(request, search: Optional[str] = None):
    
    if search:
        products = Product.objects.filter(
            is_active=True,
        ).filter(name__icontains=search) | Product.objects.filter(
            is_active=True
        ).filter(description__icontains=search)
    else:
        products = Product.objects.filter(is_active=True)
    
    return products


@router.get("/suppliers/", response={200: List[SupplierListSchema]}, tags=["Supplier"])
@paginate
def list_suppliers(request):

    suppliers = Supplier.objects.all()
    return suppliers


@router.get("/suppliers/{id}", response={200: SupplierInfoSchema}, tags=["Supplier"])
def get_supplier(request, id: str):

    supplier = get_object_or_404(Supplier, id=id)
    return supplier


@router.get("/warehouses/", response={200: List[WarehouseListSchema]}, tags=["Warehouse"])
@paginate
def list_warehouses(request):

    warehouses = Warehouse.objects.all()
    return warehouses


@router.get("/warehouses/{id}", response={200: WarehouseInfoSchema}, tags=["Warehouse"])
def get_warehouse(request, id: str):

    warehouse = get_object_or_404(Warehouse, id=id)
    return warehouse


@router.get("/stocks/", response={200: List[StockDetailSchema]}, tags=["Stock [Product <=> Warehouse]"])
@paginate
def list_stock_details(request):

    stocks = Stock.objects.all()
    return stocks