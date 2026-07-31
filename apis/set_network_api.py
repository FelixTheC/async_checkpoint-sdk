from config import Config
from aiohttp import ClientSession
from models.network_request_edit import NetworkRequestEdit
from models.network_reply import NetworkReply


async def set_network(
    client: ClientSession, data: NetworkRequestEdit, config: Config, **kwargs
) -> NetworkReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : NetworkRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NetworkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-network"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NetworkReply(**resp)
