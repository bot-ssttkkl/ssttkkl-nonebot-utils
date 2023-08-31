from functools import wraps
from typing import Optional

from nonebot_plugin_saa import MessageFactory, Text

from ..errors.error_handler import ErrorHandlers

DEFAULT_ERROR_HANDLERS = ErrorHandlers()


def handle_error(handlers: Optional[ErrorHandlers] = None,
                 silently: bool = False):
    if handlers is None:
        handlers = DEFAULT_ERROR_HANDLERS

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async def receive_error_message(msg: str):
                if not silently:
                    await MessageFactory(Text(msg)).send(reply=True)

            async with handlers.run_excepting(receive_error_message):
                return await func(*args, **kwargs)

        return wrapper

    return decorator
