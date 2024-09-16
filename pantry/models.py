from django.db import models
from categories.models import Categories
from users.models import User

class Pantry(models.Model):
    quantity = models.CharField(max_length = 20)
    item = models.CharField(max_length = 20)
    users = models.ManyToManyField(User)
    category = models.ManyToManyField(Categories)



    def __str__(self):
        return f"{self.quantity} {self.item}"

# Create your models here.
