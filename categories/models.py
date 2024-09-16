# from django.db import models



from django.db import models

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.updated_at}"

class FoodItems(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, related_name='food_items', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (Category: {self.category.name})"
