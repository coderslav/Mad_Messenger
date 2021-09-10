from rest_framework.serializers import ModelSerializer, StringRelatedField
from chat.models import User, Room


class DetailUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'avatar']


class PublicRoomsSerializer(ModelSerializer):
    participants = StringRelatedField(many=True)

    class Meta:
        model = Room
        fields = ['name', 'participants']
