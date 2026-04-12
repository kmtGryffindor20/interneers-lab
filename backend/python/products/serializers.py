from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import ProductDocument, ProductCategory
from rest_framework import serializers


class ProductSerializer(DocumentSerializer):
    url = serializers.SerializerMethodField()
    # use category name for easier input/output instead of DBRef
    category = serializers.CharField(source="category.name", allow_null=True)

    class Meta:
        model = ProductDocument
        fields = "__all__"

    def get_url(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(f"/api/products/{obj.product_id}/")
        return f"/api/products/{obj.product_id}/"


class ProductCategorySerializer(DocumentSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = "__all__"

    def get_url(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(
                f"/api/products/categories/{obj.category_id}/"
            )
        return f"/api/categories/{obj.category_id}/"
