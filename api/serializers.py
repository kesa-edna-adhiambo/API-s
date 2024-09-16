from rest_framework import serializers
from ingredients.models import Ingredients
from pantry.models import Pantry



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