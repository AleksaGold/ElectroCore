from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chain/", include("chain.urls", namespace="chain")),
    path("user/", include("users.urls", namespace="user")),
]
