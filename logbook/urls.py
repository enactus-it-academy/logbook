from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("product.urls")),
    path('', include("authapp.urls")),
    path('', include('communication.urls')),
]
