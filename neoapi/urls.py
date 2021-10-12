from django.urls import path
from neoapi.views.person import personDetails, getAllPersons
from neoapi.views.city import cityDetails, getAllCities
from neoapi.views.connectors import connectPaC, connectPaP


urlpatterns = [
    path('person', personDetails),
    path('getAllPersons', getAllPersons),
    path('city', cityDetails),
    path('getAllCities', getAllCities),
    path('connectPaC', connectPaC),
    path('connectPaP', connectPaP)
]