from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from ninja.pagination import paginate, PageNumberPagination
from ninja import Query
from django.db.models import Q
from ninja.security import APIKeyHeader

from .schemas import Message, ProductListSchema, ProductInfoSchema, ProductImageSchema, CategorySchema, ProductFilterSchema
from .models import Product, ProductImage, Category, APIKey


router = Router()


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        try:
            return APIKey.objects.get(api_key=key)
        except APIKey.DoesNotExist:
            pass

header_key = ApiKey()


@router.get("/health", auth=header_key, response={200: Message, 204: None}, tags=["Product"])
def health_check(request):

    return 200, {'message': 'success'}


@router.get("/products/", auth=header_key, response={200: List[ProductListSchema]}, tags=["Product"])
@paginate(PageNumberPagination, page_size=20)
def list_products(request, filter_data: ProductFilterSchema = Query(...)):

    products = Product.objects.prefetch_related('currency').filter(is_active=filter_data.is_active) if filter_data.is_active is not None else Product.objects.all().prefetch_related('currency')

    if filter_data.search:
        products = Product.objects.filter(
            is_active=True,
        ).filter(name__icontains=filter_data.search) | Product.objects.filter(
            is_active=True
        ).filter(description__icontains=filter_data.search)

    if filter_data.min_price or filter_data.max_price:
        price_filter = []
        if filter_data.min_price:
            price_filter.append(Q(price__gte=filter_data.min_price))
        if filter_data.max_price:
            price_filter.append(Q(price__lte=filter_data.max_price))
        products = products.filter(*price_filter)

    return products


@router.get("/products/{id}/", auth=header_key, response={200: ProductInfoSchema}, tags=["Product"])
def retrieve_product(request, id: str):

    product = get_object_or_404(Product, id=id)
    return product


@router.get("/products/{id}/images/", auth=header_key, response={200: List[ProductImageSchema]}, tags=["Product"])
def retrieve_product_images(request, id: str):

    product = get_object_or_404(Product, id=id)
    images = ProductImage.objects.filter(product=product)
    return images


@router.get("/categories/", auth=header_key, response={200: List[CategorySchema]}, tags=["Product"])
@paginate(PageNumberPagination, page_size=20)
def list_categories(request):

    categories = Category.objects.all()
    return categories


@router.get("/categories/{category_id}/products/", auth=header_key, response={200: List[ProductListSchema]}, tags=["Product"])
@paginate(PageNumberPagination, page_size=20)
def list_products_by_category(request, category_id: str):
    
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(categories=category)
    return products
