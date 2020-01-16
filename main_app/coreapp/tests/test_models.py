from django.test import TestCase

class ModelTests(TestCase):

    def test_create_information(self):
        """Test creating new entry of the information"""
        productName = "Book"
        productPrice = 640
        minPrice = 1
