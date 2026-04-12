from .models import ProductDocument, ProductCategory
from django_app.repository import BaseRepository


class ProductRepository(BaseRepository):
    def add(self, item):
        category = item.get("category")
        if category:
            # if not uuid type, try to find category by name or create new one
            try:
                category_doc = ProductCategory.objects(category_id=category).first()  # type: ignore
                if category_doc:
                    item["category"] = category_doc
                else:
                    item["category"] = None
            except Exception:
                category_doc = ProductCategory.objects(name=category).first()  # type: ignore
                if category_doc:
                    item["category"] = category_doc
                else:
                    new_category = ProductCategory(name=category)
                    new_category.save()
                    item["category"] = new_category
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


class ProductCategoryRepository(BaseRepository):
    def add(self, item):
        category = ProductCategory(**item)
        category.save()
        return category

    def get(self, item_id):
        category = ProductCategory.objects(category_id=item_id).first()  # type: ignore
        return category

    def update(self, item_id, item):
        category = self.get(item_id)
        if category:
            for key, value in item.items():
                setattr(category, key, value)
            category.save()
            return category
        return None

    def delete(self, item_id):
        category = self.get(item_id)
        if category:
            category.delete()
            return True
        return False

    def list(self):
        return list(ProductCategory.objects())  # type: ignore

    def list_products_by_category(self, category_id):
        category = self.get(category_id)
        print(ProductDocument.objects(category=category_id))  # type: ignore
        if category:
            return list(ProductDocument.objects(category=category_id))  # type: ignore
        return []

    def add_product_to_category(self, category_id, product_id):
        category = self.get(category_id)
        product = ProductDocument.objects(product_id=product_id).first()  # type: ignore
        if category and product:
            product.category = category
            product.save()
            return True
        return False

    def remove_product_from_category(self, category_id, product_id):
        category = self.get(category_id)
        product = ProductDocument.objects(product_id=product_id).first()  # type: ignore
        if category and product and product.category == category:
            product.category = None
            product.save()
            return True
        return False
