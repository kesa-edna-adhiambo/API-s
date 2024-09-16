from django.urls import path,  include
from django.contrib import admin
from .views import IngredientListView, IngredientsDetailView, PantrySearchView, ShoppingListDetailView , ShoppingListView
from .views import PantryListView, PantryDetailView, ShoppingItemListView, ShoppingItemDetailView
from .views import (
    CategoriesListView,
    CategoriesDetailView,
    FoodItemsListView,
    FoodItemsByCategoryView,
    FoodItemsInCategoryDetailView
    
)
from .views import RecipeListView, FetchRecipeView

from .views import RegisterView, LoginView


urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name="ingredient_list_view"),
    path('ingredients/<int:id>/', IngredientsDetailView.as_view(), name='ingredient-detail'),
    path('pantry/', PantryListView.as_view(), name="pantry_list_view"),
    path("pantry/<int:id>/", PantryDetailView.as_view(), name='pantry-detail_view'),
    path('pantry/searches/', PantrySearchView.as_view(), name='pantry_search_view'),   
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('categories/<int:id>/', CategoriesDetailView.as_view(), name='category_detail'),
    path('food-items/', FoodItemsListView.as_view(), name='food_items_list'),
    path('categories/<int:category_id>/food-items/', FoodItemsByCategoryView.as_view(), name='food_items_by_category'),
    path('categories/<int:category_id>/food-items/<int:food_item_id>/', FoodItemsInCategoryDetailView.as_view(), name='food_item_in_category_detail'),  
    path('shopping/', ShoppingListView.as_view(), name='shopping_list_view'),
    path('shopping/<int:id>/', ShoppingListDetailView.as_view(), name='shopping_detail_view'), 
    path('shopping/items/', ShoppingItemListView.as_view(), name='shopping-item-list'),
    path('shopping/items/<int:shopping_list_item_id>/', ShoppingItemDetailView.as_view(), name='shopping-item-detail'),
     path('recipes/', RecipeListView.as_view(), name='recipe-list'),  
    path('recipes/fetch/<str:recipe_id>/', FetchRecipeView.as_view(), name='fetch-recipe'), 
     path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    
]


