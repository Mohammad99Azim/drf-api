from ast import mod
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Movie(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    overview = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count  = models.IntegerField()
    data_created_at = models.DateTimeField(auto_now_add=True)
    data_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title