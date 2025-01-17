import logging
from logging import getLogger

from channels.generic.websocket import WebsocketConsumer

logger = getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class ChatConsumer(WebsocketConsumer):
    def connect(self) -> None:
        self.accept()

    def disconnect(self, close_code) -> None:
        pass

    def receive(self, text_data: str, **kwargs) -> None:
        logger.info(f"Received: {text_data}")
        self.send(text_data=text_data)
