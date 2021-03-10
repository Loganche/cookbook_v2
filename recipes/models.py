from django.db import models
from django.contrib.auth.models import User
from siteflags.models import ModelWithFlag

# Create your models here.


class Ingredient(models.Model):
    name = name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Recipe(ModelWithFlag):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True, blank=True)

    # Recipe-Ingredient M-M
    ingredients = models.ManyToManyField(Ingredient)

    # Adding Flags to Recipe
    favourite = 10

    def favourite_mark_add(self, user, note):
        return self.set_flag(user, note=note, status=self.favourite)

    def favourite_mark_remove(self, user):
        return self.remove_flag(user, status=self.favourite)

    def favourite_mark_check(self, user):
        return self.is_flagged(user, status=self.favourite)

    def __str__(self):
        return self.name
