from django.db import models
from users.models import User

# Create your models here.
class Shopping(models.Model):
    shopping_list_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    item = models.CharField(max_length=255)
    users = models.ManyToManyField(User)


    def __str__(self):
        return f"{self.shopping_list_id} {self.item} {self.quantity}"

