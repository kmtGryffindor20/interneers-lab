from django.test import TestCase


class HelloNameViewTests(TestCase):
    def test_hello_name_view_with_name(self):
        response = self.client.get("/hello/?name=Alice")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"message": "Hello, Alice!"})

    def test_hello_name_view_without_name(self):
        response = self.client.get("/hello/")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"message": "Hello, World!"})
