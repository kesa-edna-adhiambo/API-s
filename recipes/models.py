from django.db import models

class Recipe(models.Model):
    recipe_id = models.CharField(max_length=255, primary_key=True, default=0)
    title = models.CharField(max_length=255)
    instructions = models.TextField()
    cooking_time = models.IntegerField(default=0)
    servings = models.IntegerField(blank=True, null=True)
    ingredients = models.JSONField(default=list) 

    def __str__(self):
        return f"{self.title} {self.ingredients}"
