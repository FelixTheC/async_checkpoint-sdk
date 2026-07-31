from config import Config
from aiohttp import ClientSession
from models.udp_service_request_new import UdpServiceRequestNew
from models.udp_service_reply import UdpServiceReply


async def add_service_udp(
    client: ClientSession, data: UdpServiceRequestNew, config: Config, **kwargs
) -> UdpServiceReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : UdpServiceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UdpServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-udp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UdpServiceReply(**resp)
