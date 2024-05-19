"""
GraphQL schema definition for the cookbook application.

This module defines GraphQL types and queries for interacting with
the Category and Ingredient models.
"""

# cookbook/schema.py

import graphene
from graphene_django import DjangoObjectType

from cookbook.ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    """
    GraphQL type for the Category model.

    Attributes:
    id (int): The unique identifier of the category.
    name (str): The name of the category.
    ingredients (list of IngredientType): List of ingredients in this category.
    """

    class Meta:
        """
        Meta class for CategoryType.

        Attributes:
        model (Category): The model associated with this type.
        fields (tuple): The fields to include in the type.
        """

        model = Category
        fields = ("id", "name", "ingredients")


class IngredientType(DjangoObjectType):
    """
    GraphQL type for the Ingredient model.

    Attributes:
    id (int): The unique identifier of the ingredient.
    name (str): The name of the ingredient.
    notes (str): Additional notes about the ingredient.
    category (CategoryType): The category this ingredient belongs to.
    """

    class Meta:
        """
        Meta class for IngredientType.

        Attributes:
        model (Ingredient): The model associated with this type.
        fields (tuple): The fields to include in the type.
        """

        model = Ingredient
        fields = ("id", "name", "notes", "category")


class Query(graphene.ObjectType):
    """
    Root query class for GraphQL.

    Attributes:
    all_ingredients (graphene.List): Query to get all ingredients.
    category_by_name (graphene.Field): Query to get a category by name.
    """

    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(self, _info):
        """
        Resolves the query to get all ingredients.

        Returns:
        list of IngredientType: All ingredients in the database.
        """
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(self, _info, name):
        """
        Resolves the query to get a category by name.

        Parameters:
        name (str): The name of the category to retrieve.

        Returns:
        CategoryType or None: The category if found, otherwise None.
        """
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
