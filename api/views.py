from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ingredients.models import Ingredients
from django.shortcuts import get_object_or_404
import pantry
from .serializers import IngredientSerializer, MinimalIngredientSerializer
from pantry.models import Pantry
from .serializers import PantrySerializer, MinimalPantrySerializer
from categories.models import Categories, FoodItems
from .serializers import CategoriesSerializer, FoodItemsSerializer

from shopping.models import Shopping  
from shoppingitem.models import ShoppingItem  
from .serializers import ShoppingItemSerializer 
from .serializers import Shopping_listSerializer
from rest_framework import generics
from django.http import JsonResponse
import recipes
from recipes.models import Recipe
from .serializers import RecipeSerializer


from rest_framework.permissions import AllowAny
from users.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
import logging

class IngredientListView(APIView):
    def get(self,request):
        ingredient = Ingredients.objects.all()
        serializer = IngredientSerializer(ingredient,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class IngredientsDetailView(APIView):
    # def enroll_ingredients(self, ingredient, category_id):
    #     category = Category.objects.get(id=category_id)
    #     ingredient.category.add(category)

    def post(self, request, id):
        ingredients = Ingredients.objects.get(id=id)
        action = request.data.get("action")

        # if action =="enroll":
        #     category_id = request.data.get("category")
        #     self.enroll_ingredients(ingredients.category_id)
        #     return Response(status.HTTP_201_CREATED)      

    def get(self, request, id):
        ingredients = Ingredients.objects.get(id=id)
        serializer = IngredientSerializer(Ingredients)
        return Response(serializer.data)    

    def put(self, request, id):
        ingredients =Ingredients.objects.get(id = id)
        serializer = IngredientSerializer(ingredients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)  
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        ingredient = Ingredients.objects.get(id = id)
        ingredient.delete()
        return Response(status.HTTP_202_ACCEPTED)



class PantryListView(APIView):
    def get(self,request):
        pantry = Pantry.objects.all()
        serializer = PantrySerializer(pantry,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PantrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PantrySearchView(APIView):
    def get(self, request):
        amount = request.GET.get('id', None)
        item = request.GET.get('item', None)
        pantry =Pantry.objects.all()
        if item:
            pantry = pantry.filter(item=item)
        serializer = PantrySerializer(pantry, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
        
class PantryDetailView(APIView):
    # def enroll_pantry(self, ingredient, category_id):
    #     category = Category.objects.get(id=category_id)
    #     pantry.category.add(category)

     # def enroll_pantry(self, user, user_id):
    #    user = User.objects.get(id=user_id)
    #     pantry.user.add(user)

    def post(self, request, id):
        pantry = Pantry.objects.get(id=id)
        action = request.data.get("action")

        # if action =="enroll":
        #     category_id = request.data.get("category")
        #     self.enroll_ingredients(pantry.category_id)
        #     return Response(status.HTTP_201_CREATED) 

              # if action =="enroll":
        #     user_id = request.data.get("user")
        #     self.enroll_pantry(pantry.user_id)
        #     return Response(status.HTTP_201_CREATED)     

    def get(self, request, id):
        Pantry = Pantry.objects.get(id=id)
        serializer = PantrySerializer(Pantry)
        return Response(serializer.data)    

    def put(self, request, id):
        pantry =Pantry.objects.get(id=id)
        serializer = PantrySerializer(pantry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)  
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        pantry = Pantry.objects.get(id = id)
        pantry.delete()
        return Response(status.HTTP_202_ACCEPTED)




class CategoriesListView(APIView):
    def get(self, request):
        
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

class CategoriesDetailView(APIView):
    def get(self, request, id):
        category = get_object_or_404(Categories, id=id)
        serializer = CategoriesSerializer(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = get_object_or_404(Categories, id=id)
        serializer = CategoriesSerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodItemsListView(APIView):
    def get(self, request):
        food_items = FoodItems.objects.all()
        serializer = FoodItemsSerializer(food_items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FoodItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodItemsByCategoryView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(Categories, id=category_id)
        food_items = category.food_items.all()
        serializer = FoodItemsSerializer(food_items, many=True)
        return Response(serializer.data)

class FoodItemsDetailView(APIView):
    def get(self, request, id):
        food_item = get_object_or_404(FoodItems, id=id)
        serializer = FoodItemsSerializer(food_item)
        return Response(serializer.data)

    def put(self, request, id):
        food_item = get_object_or_404(FoodItems, id=id)
        serializer = FoodItemsSerializer(instance=food_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        food_item = get_object_or_404(FoodItems, id=id)
        food_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FoodItemsInCategoryDetailView(APIView):
    def get(self, request, category_id, food_item_id):
        category = get_object_or_404(Categories, id=category_id)
        food_item = get_object_or_404(FoodItems, id=food_item_id, category=category)
        serializer = FoodItemsSerializer(food_item)
        return Response(serializer.data)

    def put(self, request, category_id, food_item_id):
        category = get_object_or_404(Categories, id=category_id)
        food_item = get_object_or_404(FoodItems, id=food_item_id, category=category)
        serializer = FoodItemsSerializer(instance=food_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id, food_item_id):
        category = get_object_or_404(Categories, id=category_id)
        food_item = get_object_or_404(FoodItems, id=food_item_id, category=category)
        food_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ShoppingListView(APIView):
    def post(self, request):
        serializer = Shopping_listSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        shopping_list = Shopping.objects.all()
        serializer = Shopping_listSerializer(shopping_list, many=True)
        return Response(serializer.data)

class ShoppingListDetailView(APIView):
    def get(self, request, shopping_list_id):
        shopping_item = get_object_or_404(Shopping, shopping_list_id=shopping_list_id)
        serializer = Shopping_listSerializer(shopping_item)
        return Response(serializer.data)

    def put(self, request, shopping_list_id):
        shopping_item = get_object_or_404(Shopping, shopping_list_id=shopping_list_id)
        serializer = Shopping_listSerializer(shopping_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, shopping_list_id):
        shopping_item = get_object_or_404(Shopping, shopping_list_id=shopping_list_id)
        shopping_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ShoppingItemListView(APIView):
    def post(self, request):
        shopping_list = Shopping.objects.first() 

        if not shopping_list:
            return Response({"error": "No available shopping list to assign."}, status=status.HTTP_400_BAD_REQUEST)

        request.data['shopping_list_id'] = shopping_list.shopping_list_id

        serializer = ShoppingItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        shopping_items = ShoppingItem.objects.all()
        serializer = ShoppingItemSerializer(shopping_items, many=True)
        return Response(serializer.data)


class ShoppingItemDetailView(APIView):
    def get(self, request, shopping_list_item_id):
        shopping_item = get_object_or_404(ShoppingItem, shopping_list_item_id=shopping_list_item_id)
        serializer = ShoppingItemSerializer(shopping_item)
        return Response(serializer.data)

    def put(self, request, shopping_list_item_id):
        shopping_item = get_object_or_404(ShoppingItem, shopping_list_item_id=shopping_list_item_id)
        if 'shopping_list_item_id' not in request.data:
            request.data['shopping_list_item_id'] = shopping_item.shopping_list_item_id
        serializer = ShoppingItemSerializer(shopping_item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, shopping_list_item_id):
        shopping_item = get_object_or_404(ShoppingItem, shopping_list_item_id=shopping_list_item_id)
        shopping_item.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)  


class RecipeListView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class FetchRecipeView(generics.GenericAPIView):
    def get(self, request, recipe_id):
        
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={recipe_id}"
        response = requests.get(url)
        
       
        if response.status_code != 200:
            return JsonResponse({'error': 'Could not fetch recipe from MealDB'}, status=500)

        data = response.json()

        if 'meals' in data and data['meals']:
            meal = data['meals'][0]
           
            ingredients = {k: v for k, v in meal.items() if k.startswith('strIngredient') and v}
            recipe = Recipe.objects.create(
                id=meal['idMeal'],
                label=meal['strMeal'],
                url=meal['strSource'],
                ingredients=list(ingredients.values()),
                image=meal['strMealThumb']
            )
            return JsonResponse(RecipeSerializer(recipe).data, status=201)
        
        return JsonResponse({'error': 'Recipe not found in MealDB'}, status=404)







from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def register_user(request):
    return render(request, 'register_user.html')  



logger = logging.getLogger(__name__)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User registered successfully: {user.email}')
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        
        logger.error(f'User registration failed: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({'error': _('Email and password are required')}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.info(f'Login attempt for non-existent user: {email}')
            return Response({'error': _('User does not exist')}, status=status.HTTP_404_NOT_FOUND)
        
        django_user = authenticate(username=email, password=password)
        if django_user:
            logger.info(f'User logged in successfully: {email}')
            return Response({}, status=status.HTTP_200_OK)
        
        logger.error(f'Login failed for user: {email}')
        return Response({'error': _('Invalid credentials')}, status=status.HTTP_401_UNAUTHORIZED)











