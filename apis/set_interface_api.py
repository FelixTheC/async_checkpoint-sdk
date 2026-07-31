from aiohttp import ClientSession

from config import Config
from models.interface_reply import InterfaceReply
from models.interface_request_edit import InterfaceRequestEdit


async def set_interface(
    client: ClientSession, data: InterfaceRequestEdit, config: Config, **kwargs
) -> InterfaceReply:
    """
    Edit existing network interface using object uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : InterfaceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InterfaceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-interface"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InterfaceReply(**resp)
