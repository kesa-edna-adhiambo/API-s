from rest_framework import serializers
from ingredients.models import Ingredients
from pantry.models import Pantry
from categories.models import Categories, FoodItems
from shopping.models import Shopping
from shoppingitem.models import ShoppingItem
from recipes.models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class MinimalIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ["id", "ingredients_name", "quantity"]


class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = ['id', 'quantity', 'item', 'users', 'category']


class MinimalPantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = [ "item", "quantity", 'users', 'category']


class FoodItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItems
        fields = ['id', 'name', 'quantity', 'category']

class CategoriesSerializer(serializers.ModelSerializer):
    food_items = FoodItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['id', 'name', 'updated_at', 'food_items']

class Shopping_listSerializer(serializers.ModelSerializer):
    class Meta:
        model =Shopping
        fields = '__all__'

class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']  

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)