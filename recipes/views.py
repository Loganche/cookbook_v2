from django.shortcuts import render
# Create your views here.
from .models import *


def new(request):
    return render(request, 'recipes/new.html')


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    ingredients = recipe.ingredients.all()

    context = {'recipe': recipe, 'ingredients': ingredients}
    return render(request, 'recipes/recipe.html', context)
