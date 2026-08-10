from aiohttp import ClientSession

from async_checkpoint_sdk.models.multicast_address_range_query_reply import (
    MulticastAddressRangeQueryReply,
)
from async_checkpoint_sdk.models.object_in_group_query_request import ObjectInGroupQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_multicast_address_ranges(
    client: ClientSession, data: ObjectInGroupQueryRequest, config: SDKConfig, **kwargs
) -> MulticastAddressRangeQueryReply:
    """
    Retrieve all objects.

    Parameters
    ----------
    client : ClientSession
    data : ObjectInGroupQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MulticastAddressRangeQueryReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-multicast-address-ranges"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MulticastAddressRangeQueryReply(**resp)
