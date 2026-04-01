from .models import ProductDocument
from django_app.repository import BaseRepository


class ProductRepository(BaseRepository):
    def add(self, item):
        product = ProductDocument(**item)
        product.save()
        return product

    def get(self, item_id):
        product = ProductDocument.objects(product_id=item_id).first()  # type: ignore
        return product

    def update(self, item_id, item):
        product = self.get(item_id)
        if product:
            for key, value in item.items():
                setattr(product, key, value)
            product.save()
            return product
        return None

    def delete(self, item_id):
        product = self.get(item_id)
        if product:
            product.delete()
            return True
        return False

    def list(self):
        return list(ProductDocument.objects())  # type: ignore
