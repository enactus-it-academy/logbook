from django.urls import path
from .views import ProductView, ProductCreateView, SellView, ProductDeleteView


urlpatterns = [
    path("view/", ProductView.as_view(), name="add"),
    path("add/", ProductCreateView.as_view(), name="create"),
    path("sell/<int:pk>/", SellView.as_view(), name='sell'),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete"),
]
