from contextlib import asynccontextmanager
from typing import Optional

from nonebot import get_bot
from nonebot.adapters.kaiheila import Event, Bot
from nonebot.adapters.kaiheila.event import PrivateMessageEvent, ChannelMessageEvent
from nonebot_plugin_session import Session


@asynccontextmanager
async def handling_reaction(session: Session, event: Optional[Event]):
    bot: Optional[Bot] = get_bot(session.bot_id)
    if bot is None or event is None:
        return

    if isinstance(event, PrivateMessageEvent):
        await bot.directMessage_addReaction(msg_id=event.msg_id, emoji=":kissing_face:")
    elif isinstance(event, ChannelMessageEvent):
        await bot.message_addReaction(msg_id=event.msg_id, emoji=":kissing_face:")

    yield
