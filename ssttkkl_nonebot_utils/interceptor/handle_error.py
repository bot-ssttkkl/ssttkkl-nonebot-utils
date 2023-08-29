from functools import wraps

from nonebot.internal.matcher import current_matcher

from ..errors.error_handler import ErrorHandlers


def handle_error(handlers: ErrorHandlers, silently: bool = False):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            matcher = current_matcher.get()

            async def receive_error(msg: str):
                if not silently:
                    await matcher.send(msg)

            async with handlers.run_excepting(receive_error):
                return await func(*args, **kwargs)

        return wrapper

    return decorator
