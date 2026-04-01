from django.test import TestCase
import mongoengine, mongomock

mongoengine.disconnect()  # Disconnect from any existing connections
mongoengine.connect(
    db="test_db",
    host=f"mongodb://root:example@localhost:27019/test_db?authSource=admin",
)
from .models import ProductDocument
from .repository import ProductRepository
from .service import ProductService


class ProductServiceTests(TestCase):
    def setUp(self):
        self.repo = ProductRepository()
        self.service = ProductService(self.repo)

    def tearDown(self):
        """Clear products after each test"""
        ProductDocument.objects.delete()  # type: ignore

    def test_create_product(self):
        product_data = {
            "name": "Test Product",
            "description": "A test product",
            "category": "Test Category",
            "price": 9.99,
            "brand": "Test Brand",
            "quantity": 100,
        }
        product = self.service.create_product(**product_data)
        self.assertIsNotNone(product)

    def test_get_product(self):
        product_data = {
            "name": "Test Product",
            "description": "A test product",
            "category": "Test Category",
            "price": 9.99,
            "brand": "Test Brand",
            "quantity": 100,
        }
        product = self.service.create_product(**product_data)
        fetched_product = self.service.get_product(product.product_id)
        self.assertIsNotNone(fetched_product)
        self.assertEqual(fetched_product.name, product_data["name"])

    def test_update_product(self):
        product_data = {
            "name": "Test Product",
            "description": "A test product",
            "category": "Test Category",
            "price": 9.99,
            "brand": "Test Brand",
            "quantity": 100,
        }
        product = self.service.create_product(**product_data)
        updated_data = {"name": "Updated Product"}
        updated_product = self.service.update_product(
            product.product_id, **updated_data
        )
        self.assertIsNotNone(updated_product)
        self.assertEqual(updated_product.name, updated_data["name"])

    def test_delete_product(self):
        product_data = {
            "name": "Test Product",
            "description": "A test product",
            "category": "Test Category",
            "price": 9.99,
            "brand": "Test Brand",
            "quantity": 100,
        }
        product = self.service.create_product(**product_data)
        result = self.service.delete_product(product.product_id)
        self.assertTrue(result)
        self.assertIsNone(self.repo.get(product.product_id))


class ProductAPITests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        """Clear products after each test"""
        ProductDocument.objects.delete()  # type: ignore

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

    def test_create_product_api(self):
        response = self.create_product()
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("product_id", data)
        self.assertEqual(data["name"], "Test Product")

    def test_get_product_api(self):
        response = self.create_product()
        product_id = response.json()["product_id"]
        response = self.client.get(f"/api/products/{product_id}/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], "Test Product")

    def test_update_product_api(self):
        response = self.create_product()
        product_id = response.json()["product_id"]
        response = self.client.patch(
            f"/api/products/{product_id}/update/",
            {"name": "Updated Product"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], "Updated Product")

    def test_delete_product_api(self):
        response = self.create_product()
        product_id = response.json()["product_id"]
        response = self.client.delete(f"/api/products/{product_id}/delete/")
        self.assertEqual(response.status_code, 204)
        response = self.client.get(f"/api/products/{product_id}/")
        self.assertEqual(response.status_code, 404)
