from rest_framework.serializers import ModelSerializer
from chat.models import User


class DetailUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'avatar']
