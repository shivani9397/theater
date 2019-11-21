from django.shortcuts import render

# Create your views here.
from .models import Movies
from .serializers import *
from rest_framework.viewsets import ModelViewSet

#GET GET/{id} POST PUT PATCH DELETE
class MoviesOperations(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerialization

class ActorsOperations(ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerialization