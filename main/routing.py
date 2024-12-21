from django.urls import path
from .consumers import ChatConsumerDemo

websocket_urlpatterns = [
  path("wss/ai-demo/", ChatConsumerDemo.as_asgi()),
]