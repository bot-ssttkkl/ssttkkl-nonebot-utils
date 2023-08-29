import importlib

from .func_manager import FuncManagerFactory

platform_func = FuncManagerFactory()

supported_platform = ("onebot.v11", "kaiheila", "qqguild")

for func_name in ("is_destination_available", "handling_reaction", "get_user_nickname"):
    try:
        func_module = importlib.import_module("ssttkkl_nonebot_utils.platform." + func_name)
        for platform in supported_platform:
            try:
                func_module = importlib.import_module(f"ssttkkl_nonebot_utils.platform.{func_name}.{platform}")
                adapter_module = importlib.import_module(f"nonebot.adapters.{platform}")
                platform_func.register(adapter_module.Adapter.get_name(), func_name, getattr(func_module, func_name))
            except ImportError:
                pass
    except ImportError:
        pass

__all__ = ("platform_func",)
