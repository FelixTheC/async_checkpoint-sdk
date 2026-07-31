from aiohttp import ClientSession

from config import Config
from models.multi_cast_address_range_reply import MultiCastAddressRangeReply
from models.multi_cast_address_range_request_new import MultiCastAddressRangeRequestNew


async def add_multicast_address_range(
    client: ClientSession, data: MultiCastAddressRangeRequestNew, config: Config, **kwargs
) -> MultiCastAddressRangeReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MultiCastAddressRangeRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MultiCastAddressRangeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-multicast-address-range"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MultiCastAddressRangeReply(**resp)
