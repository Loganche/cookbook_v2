from django.shortcuts import render

# Create your views here.

def new(request):
    return render(request, 'accounts/new.html')


def recipe(request):
    return render(request, 'accounts/recipe.html')
