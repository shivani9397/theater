from rest_framework.serializers import ModelSerializer
from .models import *


class MoviesSerialization(ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'

class ActorsSerialization(ModelSerializer):

    class Meta:
        model = Actors
        fields = '__all__'