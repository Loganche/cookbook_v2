from django.shortcuts import render, redirect
# Create your views here.
from .models import *
from .forms import RecipeForm


def new(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogues:catalogue')

    context = {'form': form}
    return render(request, 'recipes/new.html', context)


def update(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogues:catalogue')

    context = {'form': form}
    return render(request, 'recipes/new.html', context)


def delete(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('catalogues:catalogue')

    context = {'recipe': recipe}
    return render(request, 'recipes/delete.html', context)


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    ingredients = recipe.ingredients.all()

    context = {'recipe': recipe, 'ingredients': ingredients}
    return render(request, 'recipes/recipe.html', context)
