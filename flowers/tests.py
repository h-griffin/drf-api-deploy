from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Flower

class FlowerModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Flower.objects.create(
            name = 'Name of flower',
            planter = test_user,
            description = 'Words about the flower'
        )
        test_post.save()

    def test_garden_content(self):
        flower = Flower.objects.get(id=1)

        self.assertEqual(flower.name, 'Name of flower')
        self.assertEqual(str(flower.catcher), 'tester')
        self.assertEqual(flower.description, 'Words about the flower')
