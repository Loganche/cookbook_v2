from django.shortcuts import render
# Create your views here.
from recipes.models import Recipe


def catalogue(request):
    recipes = Recipe.objects.all()

    context = {'recipes': recipes}
    return render(request, 'catalogues/catalogue.html', context)


def search(request):
    return render(request, 'catalogues/search.html')
