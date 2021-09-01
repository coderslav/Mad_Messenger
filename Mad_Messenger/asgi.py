"""
ASGI config for Mad_Messenger project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# TODO удалять или не удалять этот файл? А, может, вообще удалить routing.py, перенеся его содержимое сюда?
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mad_Messenger.settings')

application = get_asgi_application()
