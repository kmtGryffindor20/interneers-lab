from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from .models import Product


class ProductSerializer(ModelSerializer):
    link = HyperlinkedIdentityField(view_name="product-detail")
    class Meta:
        model = Product
        fields = "__all__"
