from django.urls import path
from . import views

app_name='recipes'
urlpatterns = [
    path('new/', views.new, name='new'),
    path('recipe/<int:pk>/', views.recipe, name='recipe'),
]
