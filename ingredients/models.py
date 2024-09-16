from django.db import models

class Ingredients(models.Model):
    ingredients_name = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.ingredients_name}"
    

