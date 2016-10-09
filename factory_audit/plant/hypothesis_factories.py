from django.contrib.auth import get_user_model
from hypothesis.extra.django.models import models

from .models import Item


def ItemFactory():
    """
    Build Item instance using Hypothesis - this is a simple wrapper

    Would be super-helpful if it could raise when creation was not successful.
    Instead ``example`` appears to just be silent on validation failure.
    """
    return models(Item).example()


def UserFactory():
    """
    Build a Django User instance using Hypotesis.
    """
    return models(get_user_model()).example()
