from django.contrib.auth import get_user_model
from mixer.backend.django import mixer

from .models import Item


def ItemFactory():
    return mixer.blend(Item)


def UserFactory():
    return mixer.blend(get_user_model())
