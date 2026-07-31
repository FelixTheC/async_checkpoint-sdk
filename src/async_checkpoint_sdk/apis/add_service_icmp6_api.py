from aiohttp import ClientSession

from async_checkpoint_sdk.models.service_icmp6_reply import ServiceIcmp6Reply
from async_checkpoint_sdk.models.service_icmp6_request_new import ServiceIcmp6RequestNew
from config import Config


async def add_service_icmp6(
    client: ClientSession, data: ServiceIcmp6RequestNew, config: Config, **kwargs
) -> ServiceIcmp6Reply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ServiceIcmp6RequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ServiceIcmp6Reply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-icmp6"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServiceIcmp6Reply(**resp)
