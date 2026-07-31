from aiohttp import ClientSession

from async_checkpoint_sdk.models.uri_resource_reply import UriResourceReply
from async_checkpoint_sdk.models.uri_resource_request_new import UriResourceRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_resource_uri(
    client: ClientSession, data: UriResourceRequestNew, config: SDKConfig, **kwargs
) -> UriResourceReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : UriResourceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UriResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-resource-uri"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UriResourceReply(**resp)
