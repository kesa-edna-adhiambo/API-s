from django.urls import path
from .views import IngredientListView, IngredientsDetailView, PantrySearchView
from .views import PantryListView, PantryDetailView



urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name="ingredient_list_view"),
    path('ingredients/<int:id>/', IngredientsDetailView.as_view(), name='ingredient-detail'),
    path('pantry/', PantryListView.as_view(), name="pantry_list_view"),
    path("pantry/<int:id>/", PantryDetailView.as_view(), name='pantry-detail_view'),
    path('pantry/searches/', PantrySearchView.as_view(), name='pantry_search_view'),         
]