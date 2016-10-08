from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..factory_boy_factories import ItemFactory, UserFactory
from ..models import Item


class TestItemFactory(TestCase):

    def test_default(self):
        """
        Factory Boy: Plant.Item: RED (makes invalid instance with no warning)

        Factory Boy default set up has created an instance with no name and
        does not warn the user.
        """
        result = ItemFactory()

        self.assertEqual(Item.objects.count(), 1)
        with self.assertRaises(ValidationError) as cm:
            result.full_clean()
        self.assertIn('cannot be blank', str(cm.exception))


class TestUserFactory(TestCase):

    user_model = get_user_model()

    def test_default(self):
        """
        Factory Boy: User Model: RED (makes invalid instance with no warning)
        """
        result = UserFactory()

        self.assertEqual(self.user_model.objects.count(), 1)
        with self.assertRaises(ValidationError) as cm:
            result.full_clean()
        self.assertEqual(set(cm.exception.error_dict), {'password', 'username'})
