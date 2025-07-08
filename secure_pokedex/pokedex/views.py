from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from requests import get

class PokemonListView(APIView):
    def get(self, request, *args, **kwargs):
        response = get("http://127.0.0.1:8000/api/user/me/", headers=self.request.headers)
        groups = [group['name'] for group in response.json()['groups']]
        
        if not groups:
            return Response({
                "Error": "This user doesn't belong to any group. Please subscribe to a group to get pokemon data"
            }, HTTP_403_FORBIDDEN)

        pokemons = []
        for group in groups:
            response = get(f"https://pokeapi.co/api/v2/type/{group}/")
            pokemons += response.json()['pokemon']

        # As dict isn't easy to intersect, we use this trick to remove duplicates
        unique_names = []
        unique_pokemons = []
        for pokemon in pokemons:
            name = pokemon['pokemon']['name']
            if name not in unique_names:
                unique_names.append(name)
                unique_pokemons.append(pokemon)

        return Response({'pokemons': unique_pokemons}, HTTP_200_OK)

class PokemonDetailView(APIView):
    def get(self, request, *args, **kwargs):
        response = get("http://127.0.0.1:8000/api/user/me/", headers=self.request.headers)
        groups = [group['name'] for group in response.json()['groups']]
        
        if not groups:
            return Response({
                "Error": "This user doesn't belong to any group. Please subscribe to a group to get pokemon data"
            }, HTTP_403_FORBIDDEN)
        
        response = get(f"https://pokeapi.co/api/v2/pokemon/{kwargs['identifier']}/")
        if response.status_code != 200:
            return Response({'Error': response.text}, response.status_code)
        
        data = response.json()
        pokemon_types = [pokemon_type['type']['name'] for pokemon_type in data['types']]
        if not set(groups) & set(pokemon_types):
            return Response({'Error': 'Insufficient permissions to access this pokemon data'}, HTTP_403_FORBIDDEN)

        return Response(data, HTTP_200_OK)