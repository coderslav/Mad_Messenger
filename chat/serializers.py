from rest_framework import serializers
from chat.models import *


class ChatUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
