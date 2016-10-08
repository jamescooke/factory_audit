from django.contrib.auth import get_user_model
from factory_djoy import CleanModelFactory

from .models import Item


class ItemFactory(CleanModelFactory):
    class Meta:
        model = Item
