from factory_djoy import CleanModelFactory

from .models import Item


class ItemFactory(CleanModelFactory):
    class Meta:
        model = Item
