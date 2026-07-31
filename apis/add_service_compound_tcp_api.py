from aiohttp import ClientSession

from config import Config
from models.compound_tcp_service_reply import CompoundTcpServiceReply
from models.compound_tcp_service_request_new import CompoundTcpServiceRequestNew


async def add_service_compound_tcp(
    client: ClientSession, data: CompoundTcpServiceRequestNew, config: Config, **kwargs
) -> CompoundTcpServiceReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CompoundTcpServiceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CompoundTcpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-compound-tcp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CompoundTcpServiceReply(**resp)
