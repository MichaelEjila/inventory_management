from rest_framework import views, viewsets, status
from rest_framework.response import Response
from main.models import Product, Supplier, Inventory
from main.serializers import ProductSerializer, SupplierSerializer, InventorySerializer
from rest_framework.pagination import PageNumberPagination

# Custom pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().select_related('supplier')
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        """
        Create a new product.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Update product details partially.
        """
        partial = True 
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a product.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class SupplierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows suppliers to be viewed or edited.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new supplier.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Update supplier details partially.
        """
        partial = True 
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a supplier.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Supplier deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class InventoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows inventory levels to be viewed or edited.
    """
    queryset = Inventory.objects.all().select_related('product')
    serializer_class = InventorySerializer

    def create(self, request, *args, **kwargs):
        """
        Update inventory levels.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Update inventory levels partially.
        """
        partial = True 
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """
        Retrieve inventory levels for all products.
        """
        inventory_levels = self.queryset.values('product__name', 'quantity')
        return Response(inventory_levels)
        

