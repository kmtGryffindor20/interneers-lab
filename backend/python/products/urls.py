from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("create/", views.ProductCreateView.as_view(), name="product-create"),
    path(
        "create-from-csv/",
        views.CSVBulkUploadView.as_view(),
        name="product-create-from-csv",
    ),
    path(
        "<uuid:product_id>/delete/",
        views.ProductDeleteView.as_view(),
        name="product-delete",
    ),
    path(
        "<uuid:product_id>/update/",
        views.ProductUpdateView.as_view(),
        name="product-update",
    ),
    path(
        "<uuid:product_id>/", views.ProductDetailView.as_view(), name="product-detail"
    ),
    path("categories/", views.ProductCategoryListView.as_view(), name="category-list"),
    path(
        "categories/create/",
        views.ProductCategoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "categories/<uuid:category_id>/",
        views.ProductCategoryDetailView.as_view(),
        name="category-detail",
    ),
    path(
        "categories/<uuid:category_id>/delete/",
        views.ProductCategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path(
        "categories/<uuid:category_id>/update/",
        views.ProductCategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<uuid:category_id>/products/",
        views.ProductListByCategoryView.as_view(),
        name="products-by-category",
    ),
    path(
        "add-product-to-category/<uuid:category_id>/",
        views.ProductCategoryAddProductView.as_view(),
        name="add-product-to-category",
    ),
    path(
        "delete-product-from-category/<uuid:category_id>/",
        views.ProductCategoryRemoveProductView.as_view(),
        name="delete-product-from-category",
    ),
]
