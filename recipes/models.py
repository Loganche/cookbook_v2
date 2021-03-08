from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    status = models.BooleanField(default=False, null=True)
