from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from factory_djoy import UserFactory

from ..factory_djoy_factories import ItemFactory
from ..models import Item


class TestItemFactory(TestCase):

    def test_default(self):
        """
        Factory Djoy: Plant.Item: YELLOW (raises ValidationError)
        """
        with self.assertRaises(ValidationError) as cm:
            ItemFactory()

        self.assertIn('cannot be blank', str(cm.exception))
        self.assertEqual(Item.objects.count(), 0)


class TestUserFactory(TestCase):

    user_model = get_user_model()

    def test_default(self):
        """
        Factory Djoy: User Model: GREEN (makes valid instances)
        """
        result = UserFactory.create_batch(200)

        self.assertEqual(self.user_model.objects.count(), 200)
        for user in result:
            self.assertIsNone(user.full_clean())
