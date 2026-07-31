from config import Config
from aiohttp import ClientSession
from models.host_reply import HostReply
from models.host_request_edit import HostRequestEdit


async def set_host(
    client: ClientSession, data: HostRequestEdit, config: Config, **kwargs
) -> HostReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : HostRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    HostReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-host"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return HostReply(**resp)
