from nonebot import require

from ssttkkl_nonebot_utils.nonebot import log_only_if_trace


@log_only_if_trace()
def _():
    require("nonebot_plugin_gocqhttp_cross_machine_upload_file")


_()

from nonebot_plugin_gocqhttp_cross_machine_upload_file import upload_file

__all__ = ("upload_file",)
