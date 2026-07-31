from aiohttp import ClientSession

from async_checkpoint_sdk.models.if_map_reply import IfMapReply
from async_checkpoint_sdk.models.if_map_request_new import IfMapRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_if_map_server(
    client: ClientSession, data: IfMapRequestNew, config: SDKConfig, **kwargs
) -> IfMapReply:
    """
    Create new IF-MAP server.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : IfMapRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IfMapReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-if-map-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IfMapReply(**resp)
