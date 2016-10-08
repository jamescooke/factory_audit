from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from .models import Item


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
