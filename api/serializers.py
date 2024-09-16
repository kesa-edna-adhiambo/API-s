from rest_framework import serializers
from ingredients.models import Ingredients
from pantry.models import Pantry
from categories.models import Categories, FoodItems
from shopping.models import Shopping
from shoppingitem.models import ShoppingItem
from recipes.models import Recipe




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
        fields = '__all__'

class MinimalPantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = [ "item", "quantity"]


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





       