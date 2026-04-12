class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def create_product(
        self,
        name: str,
        description: str,
        category: str,
        price: float,
        brand: str,
        quantity: int,
        **kwargs
    ):
        product_data = {
            "name": name,
            "description": description,
            "category": category,
            "price": price,
            "brand": brand,
            "quantity": quantity,
        }

        if category == "":
            product_data["category"] = None

        # save product using repository
        return self.repository.add(product_data)

    def get_product(self, product_id):
        return self.repository.get(product_id)

    def update_product(self, product_id, **kwargs):
        return self.repository.update(product_id, kwargs)

    def delete_product(self, product_id):
        return self.repository.delete(product_id)

    def list_products(self):
        return self.repository.list()


class ProductCategoryService:
    def __init__(self, repository):
        self.repository = repository

    def create_category(self, name: str, description: str = "", **kwargs):
        category_data = {
            "name": name,
            "description": description,
        }
        return self.repository.add(category_data)

    def get_category(self, category_id):
        return self.repository.get(category_id)

    def update_category(self, category_id, **kwargs):
        return self.repository.update(category_id, kwargs)

    def delete_category(self, category_id):
        return self.repository.delete(category_id)

    def list_categories(self):
        return self.repository.list()

    def list_products_by_category(self, category_id):
        return self.repository.list_products_by_category(category_id)

    def add_product_to_category(self, category_id, product_id):
        return self.repository.add_product_to_category(category_id, product_id)

    def remove_product_from_category(self, category_id, product_id):
        return self.repository.remove_product_from_category(category_id, product_id)
