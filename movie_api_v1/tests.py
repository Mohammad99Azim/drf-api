from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Movie


# Create your tests here.

class MovieTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test', password='test1234')
        test_user.save()
        test_thing = Movie.objects.create(owner=test_user,title= 'Ariel',overview= 'Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don',release_date='1988-10-21',vote_average=6.768,vote_count=164)
        test_thing.save()

    def test_thing_model(self):
        thing = Movie.objects.get(pk=1)
        self.assertEqual(str(thing.owner) , 'test')
        self.assertEqual(str(thing.title) , 'Ariel')
        self.assertEqual(str(thing.overview) , 'Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don')