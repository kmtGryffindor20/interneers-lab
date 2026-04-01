from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import ProductDocument
from rest_framework import serializers


class ProductSerializer(DocumentSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = ProductDocument
        fields = "__all__"

    def get_url(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(f"/api/products/{obj.product_id}/")
        return f"/api/products/{obj.product_id}/"
