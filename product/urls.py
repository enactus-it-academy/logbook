<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
=======
from django.urls import path
from .views import ProductView, ProductCreateView, SellView, ProductDeleteView
>>>>>>> auth

from .views import ProductView

<<<<<<< HEAD
router = DefaultRouter()
router.register(r'products', ProductView)

urlpatterns = router.urls
=======
urlpatterns = [
    path("view/", ProductView.as_view(), name="add"),
    path("add/", ProductCreateView.as_view(), name="create"),
    path("sell/<int:pk>/", SellView.as_view(), name='sell'),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete"),
]
>>>>>>> auth
