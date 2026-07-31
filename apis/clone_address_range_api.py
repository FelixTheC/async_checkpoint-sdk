from aiohttp import ClientSession

from config import Config
from models.address_range_reply import AddressRangeReply
from models.address_range_request_edit import AddressRangeRequestEdit


async def clone_address_range(
    client: ClientSession, data: AddressRangeRequestEdit, config: Config, **kwargs
) -> AddressRangeReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AddressRangeRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AddressRangeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-address-range"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AddressRangeReply(**resp)
