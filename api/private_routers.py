from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from ninja.pagination import paginate, PageNumberPagination
from ninja import Query
from django.db.models import Q
from ninja.security import django_auth

from .schemas import SupplierListSchema, SupplierInfoSchema, WarehouseListSchema, WarehouseInfoSchema, StockDetailSchema
from .models import Supplier, Warehouse, Stock


router = Router()


@router.get("/suppliers/", auth=django_auth, response={200: List[SupplierListSchema]}, tags=["Supplier"])
@paginate(PageNumberPagination, page_size=20)
def list_suppliers(request):

    suppliers = Supplier.objects.all()
    return suppliers


@router.get("/suppliers/{id}", auth=django_auth, response={200: SupplierInfoSchema}, tags=["Supplier"])
def get_supplier(request, id: str):

    supplier = get_object_or_404(Supplier, id=id)
    return supplier


@router.get("/warehouses/", auth=django_auth, response={200: List[WarehouseListSchema]}, tags=["Warehouse"])
@paginate(PageNumberPagination, page_size=20)
def list_warehouses(request):

    warehouses = Warehouse.objects.all()
    return warehouses


@router.get("/warehouses/{id}", auth=django_auth, response={200: WarehouseInfoSchema}, tags=["Warehouse"])
def get_warehouse(request, id: str):

    warehouse = get_object_or_404(Warehouse, id=id)
    return warehouse


@router.get("/stocks/", auth=django_auth, response={200: List[StockDetailSchema]}, tags=["Stock [Product <=> Warehouse]"])
@paginate(PageNumberPagination, page_size=20)
def list_stock_details(request):

    stocks = Stock.objects.all()
    return stocks