from aiohttp import ClientSession

from config import Config
from models.citrix_tcp_service_reply import CitrixTcpServiceReply
from models.citrix_tcp_service_request_new import CitrixTcpServiceRequestNew


async def add_service_citrix_tcp(
    client: ClientSession, data: CitrixTcpServiceRequestNew, config: Config, **kwargs
) -> CitrixTcpServiceReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CitrixTcpServiceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CitrixTcpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-citrix-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CitrixTcpServiceReply(**resp)
