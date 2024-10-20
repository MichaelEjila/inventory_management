# main/tasks/inventory_report.py
from celery import shared_task
from ..models import Product, InventoryReport
from django.db.models import Sum

@shared_task
def generate_inventory_report():
    # Get low stock products (for example, stock < 10)
    low_stock_products = list(Product.objects.filter(inventory_level__lt=10).values('name', 'inventory_level'))

    # Calculate total stock for suppliers
    supplier_performance = list(
        Product.objects
        .values('supplier__name')
        .annotate(total_stock=Sum('inventory_level'))
    )

    # Save the report to the database
    report = InventoryReport.objects.create(
        low_stock_products=low_stock_products,
        supplier_performance=supplier_performance
    )

    return {
        'report_id': report.id,
        'low_stock_products': low_stock_products,
        'supplier_performance': supplier_performance
    }
