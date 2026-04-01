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
