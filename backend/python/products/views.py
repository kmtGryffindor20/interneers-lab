from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

IN_MEMORY_PRODUCTS = []  # This will hold our products in memory


class ProductListView(ListAPIView):
    queryset = IN_MEMORY_PRODUCTS
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            product = Product(
                **serializer.validated_data
            )  # Create a Product instance without saving to DB
            IN_MEMORY_PRODUCTS.append(
                product
            )  # Add the new product to the in-memory list
            serializer = self.get_serializer(product)  # Serialize the new product
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        product_id = kwargs.get("pk")
        product_to_delete = None
        for p in IN_MEMORY_PRODUCTS:
            if p.product_id == product_id:
                product_to_delete = p
                break
        if product_to_delete:
            IN_MEMORY_PRODUCTS.remove(
                product_to_delete
            )  # Remove the product from the in-memory list
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND
        )


class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = IN_MEMORY_PRODUCTS

    def update(self, request, *args, **kwargs):
        print("Received update request with data:", request.data)
        product_id = kwargs.get("pk")
        product_to_update = None
        for p in self.queryset:
            if p.product_id == product_id:
                product_to_update = p
                break
        if not product_to_update:
            return Response(
                {"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(
            product_to_update, data=request.data, partial=True
        )
        if serializer.is_valid():
            for key, value in serializer.validated_data.items():
                setattr(product_to_update, key, value)
            serializer = self.get_serializer(product_to_update)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        product_id = kwargs.get("pk")
        product = None
        for p in IN_MEMORY_PRODUCTS:
            if p.product_id == product_id:
                product = p
                break
        if product:
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        return Response(
            {"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND
        )
