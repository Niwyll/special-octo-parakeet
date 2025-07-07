from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UserSerializer(ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'groups']