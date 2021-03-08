from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    # Recipe-Ingredient M-M
    ingredients = models.ManyToManyField(Ingredient)

    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name
