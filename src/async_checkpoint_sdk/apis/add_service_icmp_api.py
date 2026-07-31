from aiohttp import ClientSession

from async_checkpoint_sdk.models.service_icmp_reply import ServiceIcmpReply
from async_checkpoint_sdk.models.service_icmp_request_new import ServiceIcmpRequestNew
from config import Config


async def add_service_icmp(
    client: ClientSession, data: ServiceIcmpRequestNew, config: Config, **kwargs
) -> ServiceIcmpReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ServiceIcmpRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ServiceIcmpReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-icmp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServiceIcmpReply(**resp)
