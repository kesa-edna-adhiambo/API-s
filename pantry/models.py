from django.db import models

class Pantry(models.Model):
    quantity = models.CharField(max_length = 20)
    item = models.CharField(max_length = 20)


    def __str__(self):
        return f"{self.quantity} {self.item}"

# Create your models here.
