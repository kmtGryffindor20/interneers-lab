from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    GenericAPIView,
)
from .serializers import ProductSerializer, ProductCategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

from .repository import ProductRepository, ProductCategoryRepository
from .service import ProductService, ProductCategoryService
import csv

product_repository = ProductRepository()
product_service = ProductService(product_repository)
category_repository = ProductCategoryRepository()
category_service = ProductCategoryService(category_repository)


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return product_service.list_products()


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            product = product_service.create_product(**serializer.validated_data)
            output_serializer = self.get_serializer(product)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductSerializer
    lookup_field = "product_id"

    def delete(self, request, *args, **kwargs):
        product_id = self.kwargs.get(self.lookup_field)
        success = product_service.delete_product(product_id)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )


class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductSerializer
    lookup_field = "product_id"

    def get_queryset(self):
        return product_service.list_products()

    def get_object(self):
        product_id = self.kwargs.get(self.lookup_field)
        return product_service.get_product(product_id)


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = "product_id"

    def get_queryset(self):
        return product_service.list_products()

    def retrieve(self, request, *args, **kwargs):
        product_id = self.kwargs.get(self.lookup_field)
        product = product_service.get_product(product_id)
        if product:
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )


class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return category_service.list_categories()


class ProductCategoryCreateView(CreateAPIView):
    serializer_class = ProductCategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            category = category_service.create_category(**serializer.validated_data)
            output_serializer = self.get_serializer(category)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductCategoryDeleteView(DestroyAPIView):
    serializer_class = ProductCategorySerializer
    lookup_field = "category_id"

    def delete(self, request, *args, **kwargs):
        category_id = self.kwargs.get(self.lookup_field)
        success = category_service.delete_category(category_id)
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )


class ProductCategoryUpdateView(UpdateAPIView):
    serializer_class = ProductCategorySerializer
    lookup_field = "category_id"

    def get_queryset(self):
        return category_service.list_categories()

    def get_object(self):
        category_id = self.kwargs.get(self.lookup_field)
        return category_service.get_category(category_id)


class ProductCategoryDetailView(RetrieveAPIView):
    serializer_class = ProductCategorySerializer
    lookup_field = "category_id"

    def get_queryset(self):
        return category_service.list_categories()

    def retrieve(self, request, *args, **kwargs):
        category_id = self.kwargs.get(self.lookup_field)
        category = category_service.get_category(category_id)
        if category:
            serializer = self.get_serializer(category)
            return Response(serializer.data)
        return Response(
            {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )


class ProductListByCategoryView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return category_service.list_products_by_category(category_id)


class ProductCategoryAddProductView(UpdateAPIView):
    serializer_class = ProductCategorySerializer
    lookup_field = "category_id"

    def update(self, request, *args, **kwargs):
        category_id = self.kwargs.get(self.lookup_field)
        product_id = request.data.get("product_id")
        try:
            category_service.add_product_to_category(category_id, product_id)
            return Response(status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProductCategoryRemoveProductView(UpdateAPIView):
    serializer_class = ProductCategorySerializer
    lookup_field = "category_id"

    def update(self, request, *args, **kwargs):
        category_id = self.kwargs.get(self.lookup_field)
        product_id = request.data.get("product_id")
        print(f"Removing product {product_id} from category {category_id}")  # Debug log
        try:
            category_service.remove_product_from_category(category_id, product_id)
            return Response(status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CSVBulkUploadView(GenericAPIView):
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        file = request.FILES.get("file")
        if not file:
            return Response(
                {"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Process the CSV file and create products
        decoded_file = file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            try:
                product_service.create_product(
                    name=row["name"],
                    description=row.get("description", ""),
                    category=row.get("category", ""),
                    price=float(row["price"]),
                    brand=row["brand"],
                    quantity=int(row["quantity"]),
                )
            except ValueError as e:
                # Log the error and continue processing the next row
                print(f"Error processing row {row}: {e}")
                continue

        return Response(
            {"message": "CSV processed successfully"}, status=status.HTTP_200_OK
        )
