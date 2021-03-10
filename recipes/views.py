from django.contrib import auth, messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import RecipeForm
from accounts.decorators import *


@login_required(login_url='accounts:login')
def new(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogues:catalogue')

    context = {'form': form}
    return render(request, 'recipes/new.html', context)


@login_required(login_url='accounts:login')
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


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def delete(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('catalogues:catalogue')

    context = {'recipe': recipe}
    return render(request, 'recipes/delete.html', context)


@login_required(login_url='accounts:login')
def favourite(request, pk):
    recipe = Recipe.objects.get(id=pk)

    if recipe.favourite.filter(id=request.user.id).exists():
        recipe.favourite.remove(request.user)
    else:
        recipe.favourite.add(request.user)

    return redirect('recipes:recipe', recipe.pk)


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    ingredients = recipe.ingredients.all()

    is_favourite = False
    if recipe.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    context = {'recipe': recipe, 'ingredients': ingredients, 'is_favourite': is_favourite}
    return render(request, 'recipes/recipe.html', context)
