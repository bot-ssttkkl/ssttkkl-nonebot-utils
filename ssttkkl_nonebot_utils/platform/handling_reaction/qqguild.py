from contextlib import asynccontextmanager
from typing import Optional

from nonebot import get_bot
from nonebot.adapters.qqguild import Event, Bot, MessageEvent
from nonebot_plugin_session import Session


@asynccontextmanager
async def handling_reaction(session: Session, event: Optional[Event]):
    bot: Optional[Bot] = get_bot(session.bot_id)
    if bot is None or event is None or not isinstance(event, MessageEvent):
        return

    await bot.put_message_reaction(channel_id=event.channel_id, message_id=event.id,
                                   type=2, id="128536")  # 😘

    yield
