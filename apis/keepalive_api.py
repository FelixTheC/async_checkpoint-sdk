from aiohttp import ClientSession

from config import Config
from models.keep_alive_reply import KeepAliveReply
from models.keep_alive_request import KeepAliveRequest


async def keepalive(
    client: ClientSession, data: KeepAliveRequest, config: Config, **kwargs
) -> KeepAliveReply:
    """
    Keep the session valid/alive.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : KeepAliveRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    KeepAliveReply
    """
    url = f"https://{config.server}:{config.port}/web_api/keepalive"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return KeepAliveReply(**resp)
