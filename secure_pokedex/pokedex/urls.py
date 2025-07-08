from django.urls import path
from pokedex.views import PokemonDetailView, PokemonListView

urlpatterns = [
    path('pokemon/', PokemonListView.as_view(), name="pokemon-list"),
    path('pokemon/<str:identifier>/', PokemonDetailView.as_view(), name="pokemon-detail"),
]