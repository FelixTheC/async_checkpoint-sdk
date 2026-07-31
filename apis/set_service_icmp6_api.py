from aiohttp import ClientSession

from config import Config
from models.service_icmp6_reply import ServiceIcmp6Reply
from models.service_icmp6_request_edit import ServiceIcmp6RequestEdit


async def set_service_icmp6(
    client: ClientSession, data: ServiceIcmp6RequestEdit, config: Config, **kwargs
) -> ServiceIcmp6Reply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ServiceIcmp6RequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ServiceIcmp6Reply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-service-icmp6"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServiceIcmp6Reply(**resp)
