from django.urls import path

from channel import consumers

websocket_urlpatterns = [
    path(
        r"ws/chat/<str:first_user>/<str:second_user>/", consumers.ChatConsumer.as_asgi()
    ),
]
