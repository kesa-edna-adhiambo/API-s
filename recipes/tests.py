from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Recipe

class RecipeModelTest(TestCase):
    def setUp(self):
        self.recipe_data = {
            'recipe_id': 'recipe123',
            'title': 'Test Recipe',
            'instructions': 'Step 1: Mix ingredients. Step 2: Cook.',
            'cooking_time': 30,
            'servings': 4,
            'ingredients': {'ingredient1': '100g', 'ingredient2': '200ml'}  
        }
        self.recipe = Recipe.objects.create(**self.recipe_data)

    def test_recipe_creation(self):
        self.assertTrue(isinstance(self.recipe, Recipe))
        self.assertEqual(str(self.recipe), f"{self.recipe_data['title']} {self.recipe_data['ingredients']}")

    def test_recipe_fields(self):
        self.assertEqual(self.recipe.recipe_id, self.recipe_data['recipe_id'])
        self.assertEqual(self.recipe.title, self.recipe_data['title'])
        self.assertEqual(self.recipe.instructions, self.recipe_data['instructions'])
        self.assertEqual(self.recipe.cooking_time, self.recipe_data['cooking_time'])
        self.assertEqual(self.recipe.servings, self.recipe_data['servings'])
        self.assertEqual(self.recipe.ingredients, self.recipe_data['ingredients'])

    def test_recipe_id_primary_key(self):
        self.assertEqual(Recipe._meta.get_field('recipe_id').primary_key, True)

    def test_title_max_length(self):
        max_length = Recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_cooking_time_default(self):
        new_recipe = Recipe.objects.create(recipe_id='recipe456', title='Another Recipe')
        self.assertEqual(new_recipe.cooking_time, 0)
        self.assertEqual(new_recipe.ingredients, {})  

    def test_servings_optional(self):
        new_recipe = Recipe.objects.create(recipe_id='recipe789', title='Optional Servings Recipe')
        self.assertIsNone(new_recipe.servings)
        self.assertEqual(new_recipe.ingredients, {})  

    def test_ingredients_json_field(self):
        self.recipe.ingredients = {'new_ingredient': '50g'}
        self.recipe.save()
        
        updated_recipe = Recipe.objects.get(recipe_id=self.recipe.recipe_id)
        
        self.assertEqual(updated_recipe.ingredients, {'new_ingredient': '50g'})

    def test_invalid_cooking_time(self):
        with self.assertRaises(ValidationError):
            invalid_recipe = Recipe(
                recipe_id='invalid123',
                title='Invalid Recipe',
                cooking_time=-5 
            )
            invalid_recipe.full_clean()  