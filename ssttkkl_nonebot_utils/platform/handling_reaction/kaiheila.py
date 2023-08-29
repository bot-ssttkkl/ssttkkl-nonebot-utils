from contextlib import asynccontextmanager

from nonebot.adapters.kaiheila import Event, Bot
from nonebot.adapters.kaiheila.event import PrivateMessageEvent, ChannelMessageEvent, MessageEvent
from nonebot.exception import MatcherException


async def add_reaction(bot: Bot, event: Event, emoji: str):
    if isinstance(event, PrivateMessageEvent):
        await bot.directMessage_addReaction(msg_id=event.msg_id, emoji=emoji)
    elif isinstance(event, ChannelMessageEvent):
        await bot.message_addReaction(msg_id=event.msg_id, emoji=emoji)


async def remove_reaction(bot: Bot, event: Event, emoji: str):
    if isinstance(event, PrivateMessageEvent):
        await bot.directMessage_deleteReaction(msg_id=event.msg_id, emoji=emoji, user_id=bot.self_id)
    elif isinstance(event, ChannelMessageEvent):
        await bot.message_deleteReaction(msg_id=event.msg_id, emoji=emoji, user_id=bot.self_id)


@asynccontextmanager
async def handling_reaction(bot: Bot, event: Event):
    if not isinstance(event, MessageEvent):
        return

    await add_reaction(bot, event, ":flushed_face:")  # 处理中：😳
    try:
        yield
        await add_reaction(bot, event, ":face_blowing_a_kiss:")  # 处理完毕：😘
    except BaseException as e:
        if not isinstance(e, MatcherException):
            await add_reaction(bot, event, ":loudly_crying_face:")  # 处理出错：😭
        raise e
    finally:
        await remove_reaction(bot, event, ":flushed_face:")  # 处理中：😳
