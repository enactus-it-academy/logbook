from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from communication import views

router = DefaultRouter()
router.register(r'feedbacks', views.FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
