from django.db import models

# Create your models here

class Movies(models.Model):
    mname=models.CharField(max_length=200)

    # class Meta:
    #     db_table="movie_info"



class Actors(models.Model):
    aid = models.IntegerField()
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    Mov_actor = models.ManyToManyField(Movies)

    # class Meta:
    #     db_table="actors_info"


# class Movie_actors(models.Model):
#     movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
#     actors = models.ForeignKey(Actors, on_delete=models.CASCADE)
#     releasedate = models.IntegerField()
#
#     class Meta:
#         db_table = "Movie_actors_info"
#














