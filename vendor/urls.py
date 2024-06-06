
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # IAdded the created APP urls
    path('api/',include('vendorApp.urls')),
]
