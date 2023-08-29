from contextlib import asynccontextmanager

from nonebot.adapters.qqguild import Event, Bot, MessageEvent
from nonebot.exception import MatcherException


@asynccontextmanager
async def handling_reaction(bot: Bot, event: Event):
    if not isinstance(event, MessageEvent):
        return

    await bot.put_message_reaction(channel_id=event.channel_id, message_id=event.id,
                                   type=2, id="128563")  # 处理中：😳
    try:
        yield
        await bot.put_message_reaction(channel_id=event.channel_id, message_id=event.id,
                                       type=2, id="128536")  # 处理完毕：😘
    except BaseException as e:
        if not isinstance(e, MatcherException):
            await bot.put_message_reaction(channel_id=event.channel_id, message_id=event.id,
                                           type=2, id="128557")  # 处理出错：😭
        raise e
    finally:
        await bot.delete_own_message_reaction(channel_id=event.channel_id, message_id=event.id,
                                              type=2, id="128563")  # 处理中：😳
