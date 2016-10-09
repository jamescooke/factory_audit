from django.db import models


class Item(models.Model):
    """
    Single Item with one required field 'name'

    Taken from factory_djoy README but with a reduced length of name down to
    one character to more easily force name collisions.
    https://github.com/jamescooke/factory_djoy#example
    """
    name = models.CharField(max_length=1, unique=True)
