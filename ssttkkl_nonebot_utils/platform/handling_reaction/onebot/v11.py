import asyncio
from asyncio import sleep, shield, create_task
from contextlib import asynccontextmanager
from typing import Optional

from nonebot import logger
from nonebot.adapters.onebot.v11 import Event
from nonebot_plugin_session import Session

from ...config import Config
from ...handler.pkg_context import context
from ...service.postman import Postman

conf = context.require(Config)


async def send_delayed_loading_prompt(session: Session, event: Optional[Event]):
    try:
        await sleep(conf.pixiv_loading_prompt_delayed_time)

        logger.debug(f"send delayed loading")
        await shield(context.require(Postman).post_plain_text("努力加载中", session, event))
    except asyncio.CancelledError as e:
        raise e
    except BaseException as e:
        logger.exception(e)


@asynccontextmanager
async def handling_reaction(session: Session, event: Optional[Event]):
    task = create_task(send_delayed_loading_prompt(session, event))

    try:
        yield
    finally:
        if task and not task.done():
            task.cancel()
