from config import Config
from aiohttp import ClientSession
from models.multicast_address_range_query_reply import MulticastAddressRangeQueryReply
from models.object_in_group_query_request import ObjectInGroupQueryRequest


async def show_multicast_address_ranges(
    client: ClientSession, data: ObjectInGroupQueryRequest, config: Config, **kwargs
) -> MulticastAddressRangeQueryReply:
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
    MulticastAddressRangeQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-multicast-address-ranges"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MulticastAddressRangeQueryReply(**resp)
