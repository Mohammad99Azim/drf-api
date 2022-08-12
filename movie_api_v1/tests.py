from urllib import response
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.



from .models import Movie


# Create your tests here.

class MovieAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
        username = 'testuser1',password ='pass'
        )
        testuser1.save()

        test_movie = Movie.objects.create(owner=testuser1,title= 'Ariel',overview= 'Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don',release_date='1988-10-21',vote_average=6.768,vote_count=164)
        test_movie.save()

    def test_movie_model(self):
        movie = Movie.objects.get(pk=1)
        self.assertEqual(str(movie.owner) , 'testuser1')
        self.assertEqual(str(movie.title) , 'Ariel')
        self.assertEqual(str(movie.overview) , 'Taisto Kasurinen is a Finnish coal miner whose father has just committed suicide and who is framed for a crime he did not commit. In jail, he starts to dream about leaving the country and starting a new life. He escapes from prison but things don')

    def test_get_movies_list(self):
        url = reverse('movies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movies = response.data
        self.assertEqual(len(movies),1)
        self.assertEqual(movies[0]['title'],'Ariel')
    
    def test_get_movie_by_id(self):
        url = reverse('movie_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movie = response.data
        self.assertEqual(movie['title'],'Ariel')

    def test_create_movie(self):
        url = reverse('movies')
        data = {'owner': 1,'title': 'second','overview': 'and starting a new life.','release_date':"1988-10-21",'vote_average':6.768,'vote_count':164}
        response = self.client.post(url,data)
        movies = Movie.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(movies),2)
        self.assertEqual(movies.get(id=2).title,'second')

    def test_update_movie(self):
        url = reverse('movie_detail',args=(1,))
        data = {'owner': 1,'title': 'updated','overview': 'and starting a new life.','release_date':"1988-10-21",'vote_average':6.768,'vote_count':164}
        response = self.client.put(url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movie = response.data
        self.assertEqual(movie['title'],data['title'])
        self.assertEqual(movie['overview'],data['overview'])
        self.assertEqual(movie['owner'],data['owner'])

    def test_delete_movie(self):
        url = reverse('movie_detail',args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code , status.HTTP_204_NO_CONTENT)
        movies = Movie.objects.all()
        self.assertEqual(len(movies),0)