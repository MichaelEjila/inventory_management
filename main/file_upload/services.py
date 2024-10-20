import csv
import io
from django.db import transaction
from main.models import Product
from main.serializers import ProductSerializer

class ProductService:
    @staticmethod
    def upload_products_from_csv(file):
        total_records = 0
        successful_records = 0
        errors = []

        # Read the CSV file
        file_data = file.read()
        if not file_data:
            return {"success": False, "message": "File is empty."}

        io_string = io.StringIO(file_data.decode('utf-8'))
        reader = csv.DictReader(io_string)

        products_to_create = []

        for row in reader:
            total_records += 1
            serializer = ProductSerializer(data=row)

            if serializer.is_valid():
                products_to_create.append(serializer.validated_data)
                successful_records += 1
            else:
                errors.append({"row": row, "errors": serializer.errors})

        # Use a transaction for bulk create
        if products_to_create:
            try:
                with transaction.atomic(): 
                    Product.objects.bulk_create([Product(**data) for data in products_to_create])
            except Exception as e:
                return {"success": False, "message": "Error saving products.", "details": str(e)}

        if errors:
            return {
                "success": False,
                "message": f"Processed {total_records} records: {successful_records} succeeded.",
                "errors": errors
            }

        return {
            "success": True,
            "message": f"Successfully processed {total_records} records."
        }
