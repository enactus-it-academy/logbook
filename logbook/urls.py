from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("product.urls")),
    path('', include("authapp.urls")),
]

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls'))
# ]
