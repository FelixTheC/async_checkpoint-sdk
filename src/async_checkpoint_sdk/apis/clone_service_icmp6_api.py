from aiohttp import ClientSession

from async_checkpoint_sdk.models.service_icmp6_reply import ServiceIcmp6Reply
from async_checkpoint_sdk.models.service_icmp6_request_edit import ServiceIcmp6RequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_service_icmp6(
    client: ClientSession, data: ServiceIcmp6RequestEdit, config: SDKConfig, **kwargs
) -> ServiceIcmp6Reply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : ServiceIcmp6RequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ServiceIcmp6Reply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-service-icmp6"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServiceIcmp6Reply(**resp)
