import random
from django.shortcuts import render
from .models import Recipe, Ingredient, Category

import logging


logger = logging.getLogger(__name__)


def home(request):
    recipes = Recipe.objects.order_by("?")[:5]
    return render(request, "myapp/home.html", {"recipes": recipes})
