from aiohttp import ClientSession

from config import Config
from models.api_ok_reply import ApiOkReply
from models.interface_request_delete import InterfaceRequestDelete


async def delete_interface(
    client: ClientSession, data: InterfaceRequestDelete, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete existing network interface using object uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : InterfaceRequestDelete [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-interface"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
