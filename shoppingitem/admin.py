from django.contrib import admin

# Register your models here.
from .models import ShoppingItem
admin.site.register(ShoppingItem)