"""
Models for the ingredients app in the cookbook project.

This module defines the Category and Ingredient models, which represent
categories of ingredients and individual ingredients respectively.
"""

# cookbook/ingredients/models.py

from django.db import models


class Category(models.Model):
    """
    Represents a category with a name.

    Attributes:
    name (str): The name of the category.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the category.
        """
        return str(self.name)


class Ingredient(models.Model):
    """
    Represents an ingredient with a name, notes, and a category.

    Attributes:
    name (str): The name of the ingredient.
    notes (str): Additional notes about the ingredient.
    category (Category): The category this ingredient belongs to.
    """

    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="ingredients", on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Returns a string representation of the ingredient.
        """
        return str(self.name)  # Ensure the return value is a string
