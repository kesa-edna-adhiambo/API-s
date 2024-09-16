from django.test import TestCase
from .models import Shopping

class ShoppingModelTest(TestCase):
    def setUp(self):
        self.shopping_item = Shopping.objects.create(quantity=2, item='Apples')

    def test_shopping_model_creation(self):
        self.assertEqual(self.shopping_item.quantity, 2)
        self.assertEqual(self.shopping_item.item, 'Apples')

    def test_shopping_str_method(self):
        expected_string = f"{self.shopping_item.shopping_list_id} Apples 2"
        self.assertEqual(str(self.shopping_item), expected_string)

    def test_shopping_item_update(self):
        self.shopping_item.item = 'Oranges'
        self.shopping_item.quantity = 5
        self.shopping_item.save()

        updated_item = Shopping.objects.get(shopping_list_id=self.shopping_item.shopping_list_id)
        self.assertEqual(updated_item.item, 'Oranges')
        self.assertEqual(updated_item.quantity, 5)

    def test_shopping_item_deletion(self):
        shopping_item_id = self.shopping_item.shopping_list_id
        self.shopping_item.delete()

        with self.assertRaises(Shopping.DoesNotExist):
            Shopping.objects.get(shopping_list_id=shopping_item_id)


# Create your tests here.


