from config import Config
from aiohttp import ClientSession
from models.interface_query_reply import InterfaceQueryReply
from models.interfaces_query_request import InterfacesQueryRequest


async def show_interfaces(
    client: ClientSession, data: InterfacesQueryRequest, config: Config, **kwargs
) -> InterfaceQueryReply:
    """
    Retrieve all network interfaces for specified gateway or cluster.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : InterfacesQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InterfaceQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-interfaces"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InterfaceQueryReply(**resp)
