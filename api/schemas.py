from pydantic import Field
from typing import List, Optional
from datetime import datetime
from ninja import Schema


class Message(Schema):
    message: str


class ProductImageSchema(Schema):
    id: int
    image: str
    alt_text: Optional[str] = None


class CurrencySchema(Schema):
    code: str
    symbol: str
    
    
class ProductFilterSchema(Schema):
    is_active: Optional[bool] = None
    search: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None


class ProductListSchema(Schema):
    id: str
    name: str
    sku: str
    description: Optional[str] = None
    price: float
    currency: CurrencySchema
    is_active: bool


class ProductInfoSchema(Schema):
    id: str
    name: str
    sku: str
    description: Optional[str] = None
    price: float
    currency: CurrencySchema
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    images: Optional[List[ProductImageSchema]] = Field(default_factory=list)


class CategorySchema(Schema):
    id: str 
    name: str
    slug: str


class SupplierListSchema(Schema):
    id: str
    name: str
    email: str


class SupplierInfoSchema(Schema):
    id: str
    name: str
    email: str
    phone: str
    address: str


class WarehouseListSchema(Schema):
    id: str
    name: str


class WarehouseInfoSchema(Schema):
    id: str
    name: str
    address: str


class StockDetailSchema(Schema):
    id: str
    product: ProductListSchema
    quantity: int
    warehouse: WarehouseInfoSchema
