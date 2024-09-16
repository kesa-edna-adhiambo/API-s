from django.db import models

from categories.models import Categories

class Ingredients(models.Model):
    ingredients_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    category = models.ManyToManyField(Categories)

    def __str__(self):
        return f"{self.id} {self.ingredients_name}"
    

