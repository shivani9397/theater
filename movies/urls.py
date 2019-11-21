from rest_framework.routers import SimpleRouter
from .views import *

simpleRouter = SimpleRouter()

simpleRouter.register('Movies',MoviesOperations)
simpleRouter.register('Actors',ActorsOperations)


urlpatterns = simpleRouter.urls