import typing
from logging import getLogger
from typing import List
from app.store.vk_api.dataclasses import Update, Message

if typing.TYPE_CHECKING:
    from app.web.app import Application


class BotManager:
    def __init__(self, app: "Application"):
        self.app = app
        self.bot = None
        self.logger = getLogger("handler")

    async def handle_updates(self, updates: List[Update]):
        for update in updates:
            await self.app.store.vk_api.send_message(
                Message(
                    user_id=update.object.message.from_id,
                    text="Hello!",
                )
            )
