from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ingredients.models import Ingredients
import pantry
from .serializers import IngredientSerializer, MinimalIngredientSerializer
from pantry.models import Pantry
from .serializers import PantrySerializer, MinimalPantrySerializer

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




    


