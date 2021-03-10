from django.shortcuts import render
# Create your views here.
from recipes.models import Recipe
from recipes.filters import RecipeFilter


def catalogue(request):
    recipes = Recipe.objects.all()

    context = {'recipes': recipes}
    return render(request, 'catalogues/catalogue.html', context)


def favourites(request):
    recipes = Recipe.objects.all()

    context = {'recipes': recipes}
    return render(request, 'catalogues/favourites.html', context)


def search(request):
    recipes = Recipe.objects.all()

    recipeFilter = RecipeFilter(request.GET, queryset=recipes)
    recipes = recipeFilter.qs

    context = {'recipeFilter': recipeFilter, 'recipes': recipes}
    return render(request, 'catalogues/search.html', context)
