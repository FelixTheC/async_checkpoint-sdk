from aiohttp import ClientSession

from config import Config
from models.tcp_resource_reply import TcpResourceReply
from models.tcp_resource_request_edit import TcpResourceRequestEdit


async def set_resource_tcp(
    client: ClientSession, data: TcpResourceRequestEdit, config: Config, **kwargs
) -> TcpResourceReply:
    """
    Edit existing TCP resource using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TcpResourceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TcpResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-resource-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TcpResourceReply(**resp)
