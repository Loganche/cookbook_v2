from django.contrib import auth, messages
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


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    ingredients = recipe.ingredients.all()

    # adding to favourites
    if request.user.is_authenticated:
        user = request.user
        post = request.POST

        if post.get('favourite_set'):
            # Now a user reports this article as a favourite.
            recipe.favourite_mark_add(user, note=messages.success(request, recipe.name + ' was added to Favourites for ' + user.username))

        elif post.get('favourite_remove'):
            # Or he removes a favourite flag.
            recipe.favourite_mark_remove(user)

        is_favourite = recipe.favourite_mark_check(user)

    context = {'recipe': recipe, 'ingredients': ingredients, 'is_favourite': is_favourite, 'post': post}
    return render(request, 'recipes/recipe.html', context)
