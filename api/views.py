import json
from django.db.models import Sum, Count, F
from datetime import timedelta
from django.utils import timezone


def dashboard_callback(request, context):
    from .models import Product, Stock

    # Navigation
    context['navigation'] = [
        {'title': 'API Docs', 'link': '/api/v1/docs', 'icon': 'link'},
    ]

    # Get date ranges for metrics
    today = timezone.now()
    last_7_days = today - timedelta(days=7)
    last_28_days = today - timedelta(days=28)
    last_month_start = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
    this_month_start = today.replace(day=1)

    # KPI metrics
    total_products = Product.objects.count()
    active_products = Product.objects.filter(is_active=True).count()
    low_stock = Product.objects.filter(stock_quantity__lt=10).count()

    context['kpi'] = [
        {
            'title': 'Total Products',
            'metric': total_products,
            'footer': f"{active_products} active products"
        },
        {
            'title': 'Total Stock Value',
            'metric': f"${Product.objects.aggregate(total=Sum(F('price') * F('stock_quantity')))['total'] or 0:,.2f}",
            'footer': f"{Stock.objects.aggregate(total=Sum('quantity'))['total'] or 0} items in stock"
        },
        {
            'title': 'Low Stock Alert',
            'metric': low_stock,
            'footer': 'Products need attention'
        }
    ]

    # Progress metrics
    category_distribution = Product.objects.values('categories__name').annotate(
        count=Count('id')
    ).order_by('-count')

    context['progress'] = [
        {
            'title': cat['categories__name'],
            'description': f"{cat['count']} products",
            'value': int((cat['count'] / total_products) * 100)
        } for cat in category_distribution[:8]
    ]

    return context