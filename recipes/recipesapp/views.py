from rest_framework import viewsets
from .models import Recipe
from .serializers import RecipeSerializers
# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializers
