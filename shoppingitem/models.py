from django.db import models
from shopping.models import Shopping

class ShoppingItem(models.Model):
    shopping_list_id = models.ForeignKey(Shopping, on_delete=models.CASCADE, related_name='items',) 
    shopping_list_item_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=0)
    item = models.CharField(max_length=255,default="item")

    def __str__(self): 
        return f"{self.shopping_list_id} {self.item} {self.quantity}"