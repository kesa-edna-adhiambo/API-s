from rest_framework import serializers
from ingredients.models import Ingredients
from pantry.models import Pantry
from categories.models import Categories, FoodItems




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



       