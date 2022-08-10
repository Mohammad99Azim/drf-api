from dataclasses import fields
import imp
from rest_framework import serializers

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    class Meta:
        model = Movie
        fields = ['id','owner','owner_name','title','overview','release_date','vote_average','vote_count','data_created_at','data_updated_at']
        # fields = '__all__'