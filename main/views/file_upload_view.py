from rest_framework import views, status
from main.file_upload.services import ProductService
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

class ProductUploadView(views.APIView):
    """
    API endpoint to upload a CSV file and import products.
    """
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')

        # Check for file existence and CSV format
        if not file or not file.name.endswith('.csv'):
            message = "No file uploaded." if not file else "Invalid file format. Please upload a CSV file."
            return Response({"success": False, "message": message}, status=status.HTTP_400_BAD_REQUEST)

        result = ProductService.upload_products_from_csv(file)

        if result["success"]:
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": False, "message": result["message"], "details": result.get("errors")}, status=status.HTTP_400_BAD_REQUEST)