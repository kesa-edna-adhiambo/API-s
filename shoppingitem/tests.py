from django.test import TestCase

# Create your tests here.
from shopping.models import Shopping
from .models import ShoppingItem

class ShoppingItemModelTest(TestCase):
    def setUp(self):
        self.shopping = Shopping.objects.create(quantity=2, item='Groceries')
        self.shopping_item = ShoppingItem.objects.create(
            shopping_list_id=self.shopping,
            quantity=5,
            item='Apples'
        )

    def test_shopping_item_creation(self):
        self.assertEqual(self.shopping_item.quantity, 5)
        self.assertEqual(self.shopping_item.item, 'Apples')
        self.assertEqual(self.shopping_item.shopping_list_id, self.shopping)

    def test_shopping_item_str_method(self):
        expected_string = f"{self.shopping_item.shopping_list_id} Apples 5"
        self.assertEqual(str(self.shopping_item), expected_string)

    def test_shopping_item_update(self):
        self.shopping_item.item = 'Oranges'
        self.shopping_item.quantity = 10
        self.shopping_item.save()

        updated_item = ShoppingItem.objects.get(shopping_list_item_id=self.shopping_item.shopping_list_item_id)
        self.assertEqual(updated_item.item, 'Oranges')
        self.assertEqual(updated_item.quantity, 10)

    def test_shopping_item_deletion(self):
        shopping_item_id = self.shopping_item.shopping_list_item_id
        self.shopping_item.delete()

        with self.assertRaises(ShoppingItem.DoesNotExist):
            ShoppingItem.objects.get(shopping_list_item_id=shopping_item_id)

    def test_shopping_item_with_no_quantity_or_item(self):
        shopping_item_default = ShoppingItem.objects.create(
            shopping_list_id=self.shopping
        )

        self.assertEqual(shopping_item_default.quantity, 0)
        self.assertEqual(shopping_item_default.item, 'item')