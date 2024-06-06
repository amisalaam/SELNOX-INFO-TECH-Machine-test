from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/', VendorCreateView.as_view(), name='vendor-create'),
    path('vendors/<int:vendor_id>/', VendorDetailsView.as_view(), name='vendor-detail'),

    path('purchase_order/', PoCreateView.as_view(), name='order-create'),
    path('purchase_order/<int:po_id>/', PurchaseOrderDetails.as_view(), name='order-detail'),

    path('vendors/<int:vendor_id>/performance/', PerformanceMetricsAPIView.as_view(), name='vendor_performance'),
    
    path('purchase_orders/<int:po_id>/acknowledge/', PurchaseOrderAcknowledgeView.as_view(), name='po-acknowledge'),

]