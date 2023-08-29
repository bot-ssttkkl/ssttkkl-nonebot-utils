from nonebot import get_bot
from nonebot.adapters.kaiheila import Bot
from nonebot_plugin_session import Session


async def get_user_nickname(session: Session) -> str:
    bot: Bot = get_bot(session.bot_id)
    view = await bot.user_view(user_id=session.id1, guild_id=session.id3)
    return view.nickname
