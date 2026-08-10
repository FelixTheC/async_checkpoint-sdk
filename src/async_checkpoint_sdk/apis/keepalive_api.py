from aiohttp import ClientSession

from async_checkpoint_sdk.models.keep_alive_reply import KeepAliveReply
from async_checkpoint_sdk.models.keep_alive_request import KeepAliveRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def keepalive(
    client: ClientSession, data: KeepAliveRequest, config: SDKConfig, **kwargs
) -> KeepAliveReply:
    """
    Keep the session valid/alive.

    Parameters
    ----------
    client : ClientSession
    data : KeepAliveRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    KeepAliveReply

    """
    url = f"https://{config.server}:{config.port}/web_api/keepalive"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return KeepAliveReply(**resp)
