from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import Item


class TestModels(TestCase):

    def test_empty_not_clean(self):
        """
        Item with no values does not pass validation, name is required
        """
        with self.assertRaises(ValidationError) as cm:
            Item().full_clean()

        self.assertEqual(list(cm.exception.error_dict), ['name'])
        self.assertIn('cannot be blank', str(cm.exception))

    def test_uniqueness(self):
        """
        Item with non-unique name does not pass validation, name collides
        """
        item = Item(name='B')
        item.full_clean()
        item.save()

        with self.assertRaises(ValidationError) as cm:
            Item(name='B').full_clean()

        self.assertEqual(list(cm.exception.error_dict), ['name'])
        self.assertIn('already exists', str(cm.exception))
