from django.contrib.auth import get_user_model
from django.test import TestCase
from shopping.models import Shopping
from users.models import User

class ShoppingModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )

        self.shopping_item = Shopping.objects.create(
            quantity=3,
            item='Apples'
        )
        self.shopping_item.users.add(self.user)



# Create your tests here.


