from django.test import TestCase
from .models import Show
# Create your tests here. NEVERRRRR

class TestView(TestCase):

    def setUp(self):
        self.show_1 = Show.objects.create(name = "BB")
        self.show_2 = Show.objects.create(name = "RPDR ALL STARS")

    def test_index_includes_show(self):
        """
        when the index page is accessed, we get all shows displayed
        """
        response = self.client.get("/voter/")
        self.assertContains(response, "BB")
        self.assertContains(response, "RPDR ALL STARS")

    def test_show_includes_show_1(self):
        response = self.client.get("/voter/1")
        self.assertContains(response, "BB")
        self.assertNotContains(response, "RPDR ALL STARS")

    def test_show_includes_show_2(self):
        response = self.client.get("/voter/2")
        self.assertNotContains(response, "BB")
        self.assertContains(response, "RPDR ALL STARS")

    def test_show_not_found(self):

        response = self.client.get("/voter/0")
        self.assertEquals(response.status_code, 404)
