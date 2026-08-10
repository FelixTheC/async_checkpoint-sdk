from aiohttp import ClientSession

from async_checkpoint_sdk.models.smart_console_idle_timeout_reply import (
    SmartConsoleIdleTimeoutReply,
)
from async_checkpoint_sdk.models.smart_console_idle_timeout_request_edit import (
    SmartConsoleIdleTimeoutRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_smart_console_idle_timeout(
    client: ClientSession, data: SmartConsoleIdleTimeoutRequestEdit, config: SDKConfig, **kwargs
) -> SmartConsoleIdleTimeoutReply:
    """
    Set SmartConsole idle timeout settings.

    Parameters
    ----------
    client : ClientSession
    data : SmartConsoleIdleTimeoutRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    SmartConsoleIdleTimeoutReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-smart-console-idle-timeout"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SmartConsoleIdleTimeoutReply(**resp)
