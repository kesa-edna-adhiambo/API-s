from django.test import TestCase
from .models import Pantry

class PantryModelTest(TestCase):
    def setUp(self):
        Pantry.objects.create(quantity="2", item="apples")

    def test_pantry_creation(self):
        pantry_item = Pantry.objects.get(item="apples")
        self.assertEqual(pantry_item.quantity, "2")
        self.assertEqual(pantry_item.item, "apples")

    def test_pantry_str_method(self):
        pantry_item = Pantry.objects.get(item="apples")
        self.assertEqual(str(pantry_item), "2 apples")

    def test_max_length(self):
        pantry_item = Pantry(quantity="a" * 21, item="b" * 21)
        with self.assertRaises(Exception):
            pantry_item.full_clean()

    def test_blank_fields(self):
        pantry_item = Pantry(quantity="", item="")
        with self.assertRaises(Exception):
            pantry_item.full_clean()


# Create your tests here.
