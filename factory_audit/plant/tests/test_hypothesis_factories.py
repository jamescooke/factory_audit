from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from hypothesis.extra.django import TestCase

from ..hypothesis_factories import ItemFactory, UserFactory
from ..models import Item


class TestItemFactory(TestCase):

    def test_default(self):
        """
        Hypothesis[django]: Plant.Item: RED (does not reliably create instances)

        If the factory is called 200 times, the number of created instances is
        less than 200. You usually get around 170 items created and instead
        items are duplicated in the result list.
        """
        result = [ItemFactory() for _ in range(200)]

        self.assertEqual(len(result), 200)
        ids = {item.id for item in result}
        self.assertEqual(len(ids), max(ids))
        self.assertLess(max(ids), 180)
        self.assertLess(Item.objects.count(), 200)


class TestUserFactory(TestCase):

    user_model = get_user_model()

    def test_default(self):
        """
        Hypothesis[django]: User Model: RED (makes invalid instance)

        Hypothesis doesn't reliably create invalid instances - only about ⅓ of
        the time, usually from invalid email addresses. So run the test until a
        bad instance is created and inspect the exception raised. At least one
        instance is always saved to the database in an invalid state.
        """
        with self.assertRaises(ValidationError) as cm:
            for expected_num_created in range(1, 11):
                UserFactory().full_clean()

        self.assertEqual(self.user_model.objects.count(), expected_num_created)
        self.assertIn('valid email', str(cm.exception))
