from django.core.management.base import BaseCommand
from requests import get
from poke_manager.models import PokemonType

class Command(BaseCommand):
    help = "Run this command to initialize pokemon types"

    def handle(self, *args, **kwargs):
        types = []
        types_url = "https://pokeapi.co/api/v2/type"
        while types_url:
            response = get(types_url).json()
            types += response['results']
            types_url = response['next']
    
        PokemonType.objects.bulk_create(
            [PokemonType(**type) for type in types],
            ignore_conflicts=True
        )