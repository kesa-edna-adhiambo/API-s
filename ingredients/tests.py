from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Ingredients

class IngredientsModelTest(TestCase):
    def setUp(self):
        Ingredients.objects.create(ingredients_name="Salt", quantity=500)

    def test_ingredients_creation(self):
        ingredient = Ingredients.objects.get(ingredients_name="Salt")
        self.assertEqual(ingredient.ingredients_name, "Salt")
        self.assertEqual(ingredient.quantity, 500)

    def test_ingredients_str_method(self):
        ingredient = Ingredients.objects.get(ingredients_name="Salt")
        self.assertEqual(str(ingredient), f"{ingredient.id} Salt")

    def test_ingredients_name_max_length(self):
        ingredient = Ingredients(ingredients_name="A" * 21, quantity=100)
        with self.assertRaises(ValidationError):
            ingredient.full_clean()

    def test_quantity_is_integer(self):
        ingredient = Ingredients(ingredients_name="Sugar", quantity="not an integer")
        with self.assertRaises(ValidationError):
            ingredient.full_clean()

    def test_negative_quantity(self):
        ingredient = Ingredients(ingredients_name="Flour", quantity=-100)
        try:
            ingredient.full_clean()
        except ValidationError:
            self.fail("Negative quantity raised ValidationError unexpectedly!")

    def test_blank_fields(self):
        ingredient = Ingredients(ingredients_name="", quantity=None)
        with self.assertRaises(ValidationError):
            ingredient.full_clean()

# Create your tests here.
            
            
