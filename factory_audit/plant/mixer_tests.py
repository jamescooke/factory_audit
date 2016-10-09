from django.contrib.auth import get_user_model
from django.test import TestCase

from .mixer_factories import ItemFactory, UserFactory
from .models import Item


class TestItemFactory(TestCase):
    """
    Mixer is hard to work with. The leaking of RuntimeErrors into the console
    even when caught is not helpful. The pinned old version of fake-factory
    makes it incompatible with other libraries. It has to have its own test run
    which installs mixer and runs this test file, initiated by
    ``./test_mixer.sh``.
    """

    def test_default(self):
        """
        Mixer: Plant.Item: GREEN (makes valid instances)

        Is able to create about 10 unique instances for Item with single letter
        name. Sometimes this test appears to fail. It does not use any other
        characters than CAPS A-Z.
        """
        result = [ItemFactory() for _ in range(10)]

        self.assertEqual(Item.objects.count(), 10)
        for item in result:
            self.assertIsNone(item.full_clean())

    def test_raises(self):
        """
        Mixer: Plant.Item: GREEN (raises if runs out of names)

        Mixer raises if it can't find a way to generate a unique name. It also
        appears to dump the RuntimeError even though it's been caught.
        """
        with self.assertRaises(RuntimeError):
            [ItemFactory() for _ in range(25)]


class TestUserFactory(TestCase):

    user_model = get_user_model()

    def test_default(self):
        """
        Mixer: User Model: GREEN (makes valid instances)
        """
        result = [UserFactory() for _ in range(10)]

        self.assertEqual(self.user_model.objects.count(), 10)
        for user in result:
            self.assertIsNone(user.full_clean())
