from django.db import models


class Item(models.Model):
    """
    Single Item with one required field 'name'

    Taken from factory_djoy README
    https://github.com/jamescooke/factory_djoy#example
    """
    name = models.CharField(max_length=5, unique=True)
