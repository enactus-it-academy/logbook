from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include("product.urls")),
    path('api/', include('communication.urls')),
    path('admin/', admin.site.urls),
]
