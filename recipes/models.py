from django.db import models
from django.core.validators import MinValueValidator

class Recipe(models.Model):
    recipe_id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(default=0) 
    servings = models.IntegerField(null=True, blank=True)  
    ingredients = models.JSONField(default=dict)  

    def __str__(self):
        return f"{self.title} {self.ingredients}"