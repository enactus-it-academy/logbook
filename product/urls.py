from django.urls import path, include
from rest_framework import routers
from .views import ProductView, ProductCreateView


urlpatterns = [
    path("view/", ProductView.as_view(), name="add"),
    path("add/", ProductCreateView.as_view(), name="create"),
]
