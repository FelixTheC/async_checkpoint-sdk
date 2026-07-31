from aiohttp import ClientSession

from async_checkpoint_sdk.models.network_query_reply import NetworkQueryReply
from async_checkpoint_sdk.models.object_in_group_query_request import ObjectInGroupQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_networks(
    client: ClientSession, data: ObjectInGroupQueryRequest, config: SDKConfig, **kwargs
) -> NetworkQueryReply:
    """
    Retrieve all objects.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ObjectInGroupQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NetworkQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-networks"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NetworkQueryReply(**resp)
