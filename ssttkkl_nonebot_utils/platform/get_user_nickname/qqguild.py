from nonebot import get_bot
from nonebot.adapters.qqguild import Bot
from nonebot_plugin_session import Session


async def get_user_nickname(session: Session) -> str:
    bot: Bot = get_bot(session.bot_id)
    member = await bot.get_member(guild_id=session.id3, user_id=session.id1)
    return member.nick
