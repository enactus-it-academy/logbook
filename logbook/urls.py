from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('communication.urls')),
    path('admin/', admin.site.urls),
]
