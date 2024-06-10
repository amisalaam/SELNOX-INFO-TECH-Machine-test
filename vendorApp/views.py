from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from .models import Vendor, PurchaseOrder
from django.utils import timezone



# VENDOR MANAGEMENT
class VendorCreateView(APIView):
    # API view to create and retrieve vendor information

    def post(self, request):
        # Create a new vendor
        serializer = VendorCreateSerializers(data=request.data)
        if serializer.is_valid():
            vendor = serializer.save()
            response_data = {
                **serializer.data,
                'vendor_code': vendor.vendor_code,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Retrieve all vendors
        vendors = Vendor.objects.all()
        serializer = AllVendorSerializers(vendors, many=True)
        return Response(serializer.data)


class VendorDetailsView(APIView):
    # API view to retrieve, update, or delete a specific vendor

    def get(self, request, vendor_id):
        # Retrieve a specific vendor by ID
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AllVendorSerializers(vendor)
        return Response(serializer.data)

    def put(self, request, vendor_id):
        # Update a specific vendor by ID
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AllVendorSerializers(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vendor_id):
        # Delete a specific vendor by ID
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        vendor.delete()
        return Response({"success": "Vendor deleted successfully"}, status=status.HTTP_200_OK)


class PoCreateView(APIView):
    # API view to create and retrieve purchase orders

    def post(self, request):
        # Create a new purchase order
        serializer = PoCreateSerializer(data=request.data)
        if serializer.is_valid():
            purchase_order = serializer.save()
            response_data = {
                **serializer.data,
                'po_number': purchase_order.po_number
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Retrieve all purchase orders
        purchase_orders = PurchaseOrder.objects.all()
        serializer = AllPurachaseOrderSerilizer(purchase_orders, many=True)
        return Response(serializer.data)


class PurchaseOrderDetails(APIView):
    # API view to retrieve, update, or delete a specific purchase order

    def get(self, request, po_id):
        # Retrieve a specific purchase order by ID
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AllPurachaseOrderSerilizer(purchase_order)
        return Response(serializer.data)

    def put(self, request, po_id):
        # Update a specific purchase order by ID
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AllPurachaseOrderSerilizer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, po_id):
        # Delete a specific purchase order by ID
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)
        purchase_order.delete()
        return Response({"success": "Purchase order deleted successfully"}, status=status.HTTP_200_OK)


class PerformanceMetricsAPIView(APIView):
    # API view to retrieve vendor performance metrics

    def get(self, request, vendor_id):
        # Retrieve performance metrics for a specific vendor by ID
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        historical_performance, created = HistoricalPerformance.objects.get_or_create(vendor=vendor)
        if created or not historical_performance:
            historical_performance.calculate_and_save_metrics()
        serializer = PerformanceMetricsSerializer(historical_performance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PurchaseOrderAcknowledgeView(APIView):
    def post(self, request, po_id):
        # Update acknowledgment date for a purchase order
        purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        
        # Recalculate average response time
        historical_performance, created = HistoricalPerformance.objects.get_or_create(vendor=purchase_order.vendor)
        historical_performance.calculate_and_save_metrics()
        
        return Response({"success": "Purchase order acknowledged"}, status=status.HTTP_200_OK)