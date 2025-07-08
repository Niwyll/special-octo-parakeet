from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from poke_manager.models import PokemonType
from poke_manager.serializers import UserSerializer

# Create your views here.
class AddUserToGroupView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        pokemon_type = kwargs.get('type')
        pokemon_types = [pokemon_type.name for pokemon_type in PokemonType.objects.all()]

        if pokemon_type not in pokemon_types:
            raise NotFound(f'This pokemon type does not exist. Please choose among {", ".join(pokemon_types)}')

        group, _ = Group.objects.get_or_create(name=pokemon_type)
        group.user_set.add(request.user)
        return Response({'message': f'User {request.user} added in group {group}'}, HTTP_200_OK)

class RemoveUserFromGroupView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, **kwargs):
        pokemon_type = kwargs.get('type')
        pokemon_types = [pokemon_type.name for pokemon_type in PokemonType.objects.all()]

        if pokemon_type not in pokemon_types:
            raise NotFound(f'This pokemon type does not exist. Please choose among {", ".join(pokemon_types)}')

        group, _ = Group.objects.get_or_create(name=pokemon_type)
        group.user_set.remove(request.user)
        return Response({'message': f'User {request.user} removed from group {group}'}, HTTP_200_OK)

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user