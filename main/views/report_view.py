# main/views/inventory_report.py
from rest_framework import views, status
from rest_framework.response import Response
from ..tasks.inventory_report import generate_inventory_report
from celery.result import AsyncResult
from ..models import InventoryReport

class InventoryReportView(views.APIView):
    """
    API endpoint to generate inventory reports.
    """

    def post(self, request, *args, **kwargs):
        # Trigger the report generation task
        task = generate_inventory_report.delay()
        return Response({"success": True, "task_id": task.id}, status=status.HTTP_202_ACCEPTED)

class TaskStatusView(views.APIView):
    def get(self, request, task_id):
        task_result = AsyncResult(task_id)
        return Response({
            "task_id": task_id,
            "status": task_result.status,
            "result": task_result.result
        })

class ReportDetailView(views.APIView):
    def get(self, request, report_id):
        try:
            report = InventoryReport.objects.get(id=report_id)
            return Response({
                "success": True,
                "report": {
                    "generated_at": report.generated_at,
                    "low_stock_products": report.low_stock_products,
                    "supplier_performance": report.supplier_performance,
                }
            }, status=status.HTTP_200_OK)
        except InventoryReport.DoesNotExist:
            return Response({"success": False, "message": "Report not found."}, status=status.HTTP_404_NOT_FOUND)
