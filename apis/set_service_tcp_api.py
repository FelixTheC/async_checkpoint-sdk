from aiohttp import ClientSession

from config import Config
from models.tcp_service_reply import TcpServiceReply
from models.tcp_service_request_edit import TcpServiceRequestEdit


async def set_service_tcp(
    client: ClientSession, data: TcpServiceRequestEdit, config: Config, **kwargs
) -> TcpServiceReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TcpServiceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TcpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-service-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TcpServiceReply(**resp)
