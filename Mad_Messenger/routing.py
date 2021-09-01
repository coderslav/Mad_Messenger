from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns
# TODO раскомментировать закомментированное?
# from django.core.asgi import get_asgi_application
# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myChat.settings')

application = ProtocolTypeRouter({
    # "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
