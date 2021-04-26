from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("product.urls")),
    path('api/', include('communication.urls')),
    path('api/auth/', include("authapp.urls")),
]
