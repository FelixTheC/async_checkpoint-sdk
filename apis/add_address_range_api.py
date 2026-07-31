from config import Config
from aiohttp import ClientSession
from models.address_range_request_new import AddressRangeRequestNew
from models.address_range_reply import AddressRangeReply


async def add_address_range(
    client: ClientSession, data: AddressRangeRequestNew, config: Config, **kwargs
) -> AddressRangeReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AddressRangeRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AddressRangeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-address-range"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AddressRangeReply(**resp)
