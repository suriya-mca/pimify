# Python standard library imports
from datetime import datetime, date
from typing import List, Optional

# Third-party imports
from ninja import Schema
from pydantic import Field

# Basic message schema
class Message(Schema):
    """Schema for simple message responses."""
    message: str


class OrganizationDetailSchema(Schema):
    id: int
    name: str
    description: Optional[str] = None
    founded_date: Optional[date] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    website: Optional[str] = None


# Product-related schemas
class ProductImageSchema(Schema):
    """Schema for product image details."""
    id: int
    image: str
    alt_text: Optional[str] = None


class ProductFilterSchema(Schema):
    """
    Schema for product filtering parameters.
    Supports filtering by active status, search term, and price range.
    """
    is_active: Optional[bool] = None
    search: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None


class ProductListSchema(Schema):
    """Schema for basic product information in list views."""
    id: str
    name: str
    sku: str
    description: Optional[str] = None
    price: float
    is_active: bool


class ProductInfoSchema(Schema):
    """
    Schema for detailed product information.
    Includes all basic fields plus stock, timestamps, and related images.
    """
    id: str
    name: str
    sku: str
    description: Optional[str] = None
    price: float
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    images: Optional[List[ProductImageSchema]] = Field(default_factory=list)


# Category schemas
class CategorySchema(Schema):
    """Schema for product categories."""
    id: str 
    name: str
    slug: str


# Supplier schemas
class SupplierListSchema(Schema):
    """Schema for basic supplier information in list views."""
    id: str
    name: str
    email: str


class SupplierInfoSchema(Schema):
    """Schema for detailed supplier information."""
    id: str
    name: str
    email: str
    phone: str
    address: str


# Warehouse schemas
class WarehouseListSchema(Schema):
    """Schema for basic warehouse information in list views."""
    id: str
    name: str


class WarehouseInfoSchema(Schema):
    """Schema for detailed warehouse information."""
    id: str
    name: str
    address: str


# Relationship schemas
class StockDetailSchema(Schema):
    """
    Schema for stock details.
    Represents the relationship between products and warehouses.
    """
    id: str
    product: ProductListSchema
    quantity: int
    warehouse: WarehouseInfoSchema


class PprductSupplierDetails(Schema):
    """
    Schema for product-supplier relationship details.
    Includes cost and lead time information.
    """
    id: str
    product: ProductListSchema
    supplier: SupplierInfoSchema
    cost_price: float
    lead_time: int