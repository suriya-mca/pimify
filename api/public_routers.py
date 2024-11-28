# Python standard library imports
from typing import List

# Django imports
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Django Ninja imports
from ninja import Router, Query
from ninja.pagination import paginate, PageNumberPagination
from ninja.security import APIKeyHeader

# Local imports
from .models import Product, ProductImage, Category, APIKey, Organization
from .schemas import (
    Message,
    ProductListSchema,
    ProductInfoSchema,
    ProductImageSchema,
    CategorySchema,
    ProductFilterSchema,
    OrganizationDetailSchema
)

# Initialize router
router = Router()

# Custom API Key authentication
class ApiKey(APIKeyHeader):
    """Custom API Key authentication using header."""
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        """Validate API key against database."""
        try:
            return APIKey.objects.get(api_key=key)
        except APIKey.DoesNotExist:
            pass

# Initialize API key authentication
header_key = ApiKey()

# Health check endpoint
@router.get("/health",
            response={200: Message, 204: None}, 
            tags=["Product"])
def health_check(request):
    """Simple health check endpoint to verify API status."""
    return 200, {'message': 'success'}

# Retrieve organization details endpoint
@router.get("/organization",
            response=OrganizationDetailSchema,
            tags=["Organization"])
def get_organization_details(request):
    try:
        # Get organization from database
        organization = Organization.objects.get()
        return organization
    except Organization.DoesNotExist:
        # Handle case when no organization is found
        return {"error": "Organization details not found"}, 404

# Product endpoints
@router.get("/products/", 
            auth=header_key, 
            response={200: List[ProductListSchema]}, 
            tags=["Product"])
@paginate(PageNumberPagination, page_size=20)
def list_products(request, filter_data: ProductFilterSchema = Query(...)):
    """
    Get paginated list of products with optional filtering.
    Supports filtering by active status, price range, and search term.
    """
    # Base query with active status filter
    products = (Product.objects.prefetch_related('currency')
               .filter(is_active=filter_data.is_active) 
               if filter_data.is_active is not None 
               else Product.objects.all().prefetch_related('currency'))

    # Search filter
    if filter_data.search:
        products = Product.objects.filter(
            is_active=True,
            name__icontains=filter_data.search
        ) | Product.objects.filter(
            is_active=True,
            description__icontains=filter_data.search
        )

    # Price range filter
    if filter_data.min_price or filter_data.max_price:
        price_filter = []
        if filter_data.min_price:
            price_filter.append(Q(price__gte=filter_data.min_price))
        if filter_data.max_price:
            price_filter.append(Q(price__lte=filter_data.max_price))
        products = products.filter(*price_filter)

    return products


@router.get("/products/{id}/", 
            auth=header_key, 
            response={200: ProductInfoSchema}, 
            tags=["Product"])
def retrieve_product(request, id: str):
    """Get detailed information about a specific product."""
    product = get_object_or_404(Product, id=id)
    return product


@router.get("/products/{id}/images/", 
            auth=header_key, 
            response={200: List[ProductImageSchema]}, 
            tags=["Product"])
def retrieve_product_images(request, id: str):
    """Get all images associated with a specific product."""
    product = get_object_or_404(Product, id=id)
    images = ProductImage.objects.filter(product=product)
    return images

# Category endpoints
@router.get("/categories/", 
            auth=header_key, 
            response={200: List[CategorySchema]}, 
            tags=["Product"])
@paginate(PageNumberPagination, page_size=20)
def list_categories(request):
    """Get paginated list of all product categories."""
    categories = Category.objects.all()
    return categories


@router.get("/categories/{category_id}/products/", 
            auth=header_key, 
            response={200: List[ProductListSchema]}, 
            tags=["Product"])
@paginate(PageNumberPagination, page_size=20)
def list_products_by_category(request, category_id: str):
    """Get paginated list of products in a specific category."""
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(categories=category)
    return products