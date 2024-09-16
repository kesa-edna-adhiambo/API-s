from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError  # Import IntegrityError
from .models import User

class UserModelTest(TestCase):
    
    def setUp(self):
        # Create a user instance for use in the tests
        self.user = User(
            first_name='John',
            last_name='Doe',
            password='securepassword',
            email='john.doe@example.com'
        )
    
    def test_user_creation(self):
        # Test creating a valid user
        self.user.save()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'john.doe@example.com')
    
    def test_user_string_representation(self):
        # Test the string representation of the User
        self.user.save()
        self.assertEqual(str(self.user), 'John Doe')

    def test_user_password_length(self):
        # Test password length constraint
        user = User(
            first_name='Jane',
            last_name='Doe',
            password='a' * 17,  # Password is 17 characters long, which should be invalid
            email='jane.doe@example.com'
        )
        with self.assertRaises(ValidationError):
            user.full_clean()  # This will validate the model fields

    def test_user_unique_email(self):
        # Test the unique constraint on the email field
        user1 = User(
            first_name='Alice',
            last_name='Smith',
            password='password123',
            email='alice.smith@example.com'
        )
        user1.save()
        user2 = User(
            first_name='Bob',
            last_name='Brown',
            password='password456',
            email='alice.smith@example.com'  # Duplicate email
        )
        try:
            user2.save()
            self.fail("IntegrityError not raised due to duplicate email")
        except IntegrityError:
            pass

    def test_user_missing_required_fields(self):
        # Test missing required fields
        user = User(
            first_name='',  # This should be an empty string
            last_name='Doe',
            password='password123',
            email='missing.first.name@example.com'
        )
        with self.assertRaises(ValidationError):
            user.full_clean()  # This will validate the model fields

        user = User(
            first_name='Jane',
            last_name='Doe',
            password='a' * 17,  # Ensure this is more than 16 characters
            email='missing.password@example.com'
        )
        with self.assertRaises(ValidationError):
            user.full_clean()  # This will validate the model fields
