from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.inventory_view import ProductViewSet, SupplierViewSet, InventoryViewSet
from .views.file_upload_view import ProductUploadView
from main.views.report_view import InventoryReportView, ReportDetailView, TaskStatusView

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = [
    path('', include(router.urls)),
    path('upload-products/', ProductUploadView.as_view(), name='upload-products'), 
    path('reports/inventory/', InventoryReportView.as_view(), name='inventory-report'),
    path('reports/status/<str:task_id>/', TaskStatusView.as_view(), name='task-status'),
    path('reports/<int:report_id>/', ReportDetailView.as_view(), name='report-detail'),
]
