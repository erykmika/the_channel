import json
import logging
from logging import getLogger

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

logging.basicConfig(level=logging.INFO)


class ChatConsumer(WebsocketConsumer):

    def __init__(
        self, logger: logging.Logger = getLogger(__name__), *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self._logger = logger
        self._room_name = None

    def connect(self) -> None:
        first_user = self.scope["url_route"]["kwargs"]["first_user"]
        second_user = self.scope["url_route"]["kwargs"]["second_user"]
        users_sorted = sorted(
            (first_user, second_user)
        )  # Need to sort room users to ensure they are in the same order on each client
        self._room_name = f"room_{users_sorted[0]}_{users_sorted[1]}"
        async_to_sync(self.channel_layer.group_add)(self._room_name, self.channel_name)
        self._logger.info(f"Added current channel to channels group: {self._room_name}")
        self.accept()

    def disconnect(self, close_code) -> None:
        async_to_sync(self.channel_layer.group_discard)(
            self._room_name, self.channel_name
        )

    def receive(self, text_data: str, **kwargs) -> None:
        message = json.loads(text_data)["message"]
        message_user = self.scope["user"].username
        message = f"[{message_user}] : {message}"
        self._logger.info(f"Received: {message}")
        async_to_sync(self.channel_layer.group_send)(
            self._room_name, {"type": "chat.message", "message": message}
        )

    def chat_message(self, event) -> None:
        self._logger.info(f"Received chat message event: {event}")
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))
