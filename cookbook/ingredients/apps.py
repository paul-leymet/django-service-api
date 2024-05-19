"""
This module provides an example of how to add a module docstring
to satisfy the Pylint warning C0114.

It includes a sample function `foo` and a sample class `Bar`.
"""

from django.apps import AppConfig


class IngredientsConfig(AppConfig):
    """
    <Brief description of the class's purpose and functionality.>

    Attributes:
    <attribute name> (<type>): <description of the attribute>

    Methods:
    <method name>: <description of the method>
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "cookbook.ingredients"
