import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

from main.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": application,
    "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
})
