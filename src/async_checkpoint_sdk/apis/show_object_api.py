from aiohttp import ClientSession

from async_checkpoint_sdk.models.show_object_reply import ShowObjectReply
from async_checkpoint_sdk.models.show_object_request import ShowObjectRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_object(
    client: ClientSession, data: ShowObjectRequest, config: SDKConfig, **kwargs
) -> ShowObjectReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : ShowObjectRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ShowObjectReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShowObjectReply(**resp)
