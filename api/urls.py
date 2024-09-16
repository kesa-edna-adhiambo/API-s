from django.urls import path
from .views import IngredientListView, IngredientsDetailView, PantrySearchView
from .views import PantryListView, PantryDetailView
from .views import (
    CategoriesListView,
    CategoriesDetailView,
    FoodItemsListView,
    FoodItemsByCategoryView,
    FoodItemsInCategoryDetailView
)



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
]