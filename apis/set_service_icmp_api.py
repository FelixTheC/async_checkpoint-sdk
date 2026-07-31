from aiohttp import ClientSession

from config import Config
from models.service_icmp_reply import ServiceIcmpReply
from models.service_icmp_request_edit import ServiceIcmpRequestEdit


async def set_service_icmp(
    client: ClientSession, data: ServiceIcmpRequestEdit, config: Config, **kwargs
) -> ServiceIcmpReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ServiceIcmpRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ServiceIcmpReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-service-icmp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServiceIcmpReply(**resp)
