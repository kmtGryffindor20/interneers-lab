from django.test import TestCase


class ProductTests(TestCase):
    def setUp(self):
        """Clear products before each test"""
        from products.views import IN_MEMORY_PRODUCTS

        IN_MEMORY_PRODUCTS.clear()

    def tearDown(self):
        """Clear products after each test"""
        from products.views import IN_MEMORY_PRODUCTS

        IN_MEMORY_PRODUCTS.clear()

    def create_product(
        self,
        name="Test Product",
        description="A test product",
        category="Test Category",
        price=9.99,
        brand="Test Brand",
        quantity=100,
    ):
        return self.client.post(
            "/api/products/create/",
            {
                "name": name,
                "description": description,
                "category": category,
                "price": price,
                "brand": brand,
                "quantity": quantity,
            },
            content_type="application/json",
        )

    def test_product_creation(self):
        response = self.create_product()
        self.assertEqual(response.status_code, 201)
        self.assertIn("product_id", response.json())
        self.assertEqual(response.json()["name"], "Test Product")

    def test_product_deletion(self):
        create_response = self.create_product()
        product_id = create_response.json()["product_id"]
        delete_response = self.client.delete(f"/api/products/{product_id}/delete/")
        self.assertEqual(delete_response.status_code, 204)

    def test_product_list(self):
        self.create_product(name="Product 1")
        self.create_product(name="Product 2")
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["name"], "Product 1")
        self.assertEqual(response.json()[1]["name"], "Product 2")

    def test_product_update(self):
        create_response = self.create_product()
        product_id = create_response.json()["product_id"]
        update_response = self.client.put(
            f"/api/products/{product_id}/update/",
            {
                "name": "Updated Product",
                "description": "An updated test product",
                "category": "Updated Category",
                "price": 19.99,
                "brand": "Updated Brand",
                "quantity": 50,
            },
            content_type="application/json",
        )
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["name"], "Updated Product")
        self.assertEqual(update_response.json()["price"], "19.99")

    def test_product_detail(self):
        create_response = self.create_product()
        product_id = create_response.json()["product_id"]
        detail_response = self.client.get(f"/api/products/{product_id}/")
        self.assertEqual(detail_response.status_code, 200)
        self.assertEqual(detail_response.json()["product_id"], product_id)
        self.assertEqual(detail_response.json()["name"], "Test Product")
