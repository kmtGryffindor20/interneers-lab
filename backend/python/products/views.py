from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView,
)
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

from .repository import ProductRepository
from .service import ProductService

repo = ProductRepository()
service = ProductService(repo)


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return service.list_products()


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            product = service.create_product(**serializer.validated_data)
            output_serializer = self.get_serializer(product)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductSerializer
    lookup_field = "product_id"

    def delete(self, request, *args, **kwargs):
        product_id = self.kwargs.get(self.lookup_field)
        success = service.delete_product(product_id)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )


class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductSerializer
    lookup_field = "product_id"

    def get_queryset(self):
        return service.list_products()

    def get_object(self):
        product_id = self.kwargs.get(self.lookup_field)
        return service.get_product(product_id)


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = "product_id"

    def get_queryset(self):
        return service.list_products()

    def retrieve(self, request, *args, **kwargs):
        product_id = self.kwargs.get(self.lookup_field)
        product = service.get_product(product_id)
        if product:
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )
