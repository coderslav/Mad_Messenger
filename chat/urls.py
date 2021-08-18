from django.urls import path
from chat.views import *

urlpatterns = [
    path('user/create/', CreateChatUserViewAPI.as_view(), name='create_user_api'),
]