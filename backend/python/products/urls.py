from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView,
    ProductDetailView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path(
        "<uuid:product_id>/delete/", ProductDeleteView.as_view(), name="product-delete"
    ),
    path(
        "<uuid:product_id>/update/", ProductUpdateView.as_view(), name="product-update"
    ),
    path("<uuid:product_id>/", ProductDetailView.as_view(), name="product-detail"),
]
