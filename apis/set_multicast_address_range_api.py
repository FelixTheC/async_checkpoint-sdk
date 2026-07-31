from aiohttp import ClientSession

from config import Config
from models.multi_cast_address_range_reply import MultiCastAddressRangeReply
from models.multi_cast_address_range_request_edit import MultiCastAddressRangeRequestEdit


async def set_multicast_address_range(
    client: ClientSession, data: MultiCastAddressRangeRequestEdit, config: Config, **kwargs
) -> MultiCastAddressRangeReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MultiCastAddressRangeRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MultiCastAddressRangeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-multicast-address-range"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MultiCastAddressRangeReply(**resp)
