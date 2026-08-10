from aiohttp import ClientSession

from async_checkpoint_sdk.models.uri_resource_reply import UriResourceReply
from async_checkpoint_sdk.models.uri_resource_request_edit import UriResourceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_resource_uri(
    client: ClientSession, data: UriResourceRequestEdit, config: SDKConfig, **kwargs
) -> UriResourceReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : UriResourceRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    UriResourceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-resource-uri"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UriResourceReply(**resp)
