from django.contrib.auth import get_user_model
from model_mommy import mommy

from .models import Item


def ItemFactory():
    return mommy.make(Item)


def UserFactory():
    return mommy.make(get_user_model())
