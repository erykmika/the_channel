from django.urls import path

from channel.consumers import ChatConsumer

websocket_urlpatterns = [
    path(r"ws/chat/<str:first_user>/<str:second_user>/", ChatConsumer.as_asgi()),
]
