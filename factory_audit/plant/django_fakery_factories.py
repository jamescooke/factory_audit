from django.contrib.auth import get_user_model
from django_fakery import factory

from .models import Item


def ItemFactory():
    return factory.m(Item)()


def UserFactory():
    return factory.m(get_user_model())()
