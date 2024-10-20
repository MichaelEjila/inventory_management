from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from main.models import Supplier, Product
from django.core.files.uploadedfile import SimpleUploadedFile

from unittest.mock import patch

class ProductViewSetTest(APITestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name='Supplier A', contact_info='info@suppliera.com')
        self.product = Product.objects.create(name='Product A', description='Description A', price=10.00, supplier=self.supplier)
        self.url = reverse('product-list')

    def test_list_products(self):
        response = self.client.get(self.url)

        products_by_supplier = [product for product in response.data['results'] if product['supplier'] == self.supplier.id]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(products_by_supplier), 1)

    def test_create_product(self):
        data = {
            'name': 'New Product',
            'description': 'New Description',
            'price': 20.00,
            'supplier': self.supplier.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_product(self):
        delete_url = reverse('product-detail', args=[self.product.id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class SupplierViewSetTest(APITestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name='Supplier A', contact_info='info@suppliera.com')
        self.url = reverse('supplier-list')

    def test_list_suppliers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_supplier(self):
        data = {
            'name': 'New Supplier',
            'contact_info': 'new@example.com'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_supplier(self):
        delete_url = reverse('supplier-detail', args=[self.supplier.id]) 
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# class ProductUploadViewTest(APITestCase):
#     def setUp(self):
#         self.url = reverse('upload-products')

    
#     @patch('main.file_upload.services.ProductService.upload_products_from_csv')
#     def test_upload_valid_csv(self, mock_upload_products_from_csv):
#         csv_data = b'name,description,price,supplier\nProduct 1,Description 1,10.00,1'
#         file = SimpleUploadedFile('products.csv', csv_data, content_type='text/csv')

#         mock_upload_products_from_csv.return_value = {"success": True}

#         response = self.client.post(self.url, {'file': file}, format='multipart')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         mock_upload_products_from_csv.assert_called_once_with(file)

#     def test_upload_invalid_file_format(self):
#         file = SimpleUploadedFile('products.txt', b'invalid format', content_type='text/plain')
        
#         response = self.client.post(self.url, {'file': file}, format='multipart')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data['message'], 'Invalid file format. Please upload a CSV file.')


class InventoryReportViewTest(APITestCase):
    @patch('main.tasks.inventory_report.generate_inventory_report.delay')
    def test_generate_report(self, mock_generate_inventory_report):
        url = reverse('inventory-report') 
        
        mock_generate_inventory_report.return_value.id = 'fake-task-id'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['task_id'], 'fake-task-id')