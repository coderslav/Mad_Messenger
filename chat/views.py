from django.shortcuts import render
from chat.models import *
from rest_framework import generics
from chat.serializers import *


# Create your views here.
class CreateChatUserViewAPI(generics.CreateAPIView):
    serializer_class = ChatUserDetailsSerializer
