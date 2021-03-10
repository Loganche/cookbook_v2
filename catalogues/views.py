from django.shortcuts import render
# Create your views here.
from recipes.models import Recipe
from recipes.filters import RecipeFilter


def catalogue(request):
    recipes = Recipe.objects.all()

    is_favourite = False
    for recipe in recipes:
        if recipe.favourite.filter(id=request.user.id).exists():
            is_favourite = True

    context = {'recipes': recipes, 'is_favourite': is_favourite}
    return render(request, 'catalogues/catalogue.html', context)


def favourites(request):
    user = request.user
    recipes = user.favourite.all()

    context = {'recipes': recipes}
    return render(request, 'catalogues/favourites.html', context)


def search(request):
    recipes = Recipe.objects.all()

    is_favourite = False
    for recipe in recipes:
        if recipe.favourite.filter(id=request.user.id).exists():
            is_favourite = True

    recipeFilter = RecipeFilter(request.GET, queryset=recipes)
    recipes = recipeFilter.qs

    context = {'recipeFilter': recipeFilter, 'recipes': recipes, 'is_favourite': is_favourite}
    return render(request, 'catalogues/search.html', context)
