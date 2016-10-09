from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from ..model_mommy_factories import ItemFactory, UserFactory
from ..models import Item


class TestItemFactory(TestCase):

    def test_default(self):
        """
        Model Mommy: Plant.Item: YELLOW (raises IntegrityError)

        There is no method used to create unique values so there are collisions
        when there are a small number of possible values. The "result" item
        does not pass validation.
        """
        with self.assertRaises(IntegrityError) as cm:
            for expected_num_created in range(1, 25):
                with transaction.atomic():
                    ItemFactory()

        self.assertEqual(Item.objects.count(), expected_num_created - 1)
        self.assertIn('UNIQUE', str(cm.exception))


class TestUserFactory(TestCase):

    user_model = get_user_model()

    def test_default(self):
        """
        Model Mommy: User Model: GREEN (makes valid instances)

        Creates users with no first_name, last_name or email address but these
        are not required fields by default. Instead, creates users with long
        random usernames that are very unlikely to collide.
        """
        result = [UserFactory() for _ in range(10)]

        self.assertEqual(self.user_model.objects.count(), 10)
        for user in result:
            self.assertIsNone(user.full_clean())
