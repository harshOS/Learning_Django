from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
     
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)

    # def test_about_page_fail(self):
    #     response = self.client.get('/contact/')
    #     self.assertEqual(response.status_code,404)
