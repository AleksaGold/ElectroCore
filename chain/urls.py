from django.urls import path

from chain.apps import ChainConfig
from chain.views import (ChainCreateAPIView, ChainDestroyAPIView,
                         ChainListAPIView, ChainRetrieveAPIView,
                         ChainUpdateAPIView, ContactCreateAPIView,
                         ContactDestroyAPIView, ContactListAPIView,
                         ContactRetrieveAPIView, ContactUpdateAPIView,
                         ProductCreateAPIView, ProductDestroyAPIView,
                         ProductListAPIView, ProductRetrieveAPIView,
                         ProductUpdateAPIView)

app_name = ChainConfig.name

urlpatterns = [
    path("contacts/create/", ContactCreateAPIView.as_view(), name="contacts_create"),
    path("contacts/", ContactListAPIView.as_view(), name="contacts_list"),
    path(
        "contacts/retrieve/<int:pk>/",
        ContactRetrieveAPIView.as_view(),
        name="contacts_retrieve",
    ),
    path(
        "contacts/update/<int:pk>/",
        ContactUpdateAPIView.as_view(),
        name="contacts_update",
    ),
    path(
        "contacts/destroy/<int:pk>/",
        ContactDestroyAPIView.as_view(),
        name="contacts_destroy",
    ),
    path("products/create/", ProductCreateAPIView.as_view(), name="products_create"),
    path("products/", ProductListAPIView.as_view(), name="products_list"),
    path(
        "products/retrieve/<int:pk>/",
        ProductRetrieveAPIView.as_view(),
        name="products_retrieve",
    ),
    path(
        "products/update/<int:pk>/",
        ProductUpdateAPIView.as_view(),
        name="products_update",
    ),
    path(
        "products/destroy/<int:pk>/",
        ProductDestroyAPIView.as_view(),
        name="products_destroy",
    ),
    path("chains/create/", ChainCreateAPIView.as_view(), name="chains_create"),
    path("chains/", ChainListAPIView.as_view(), name="chains_list"),
    path(
        "chains/retrieve/<int:pk>/",
        ChainRetrieveAPIView.as_view(),
        name="chains_retrieve",
    ),
    path("chains/update/<int:pk>/", ChainUpdateAPIView.as_view(), name="chains_update"),
    path(
        "chains/destroy/<int:pk>/", ChainDestroyAPIView.as_view(), name="chains_destroy"
    ),
]
