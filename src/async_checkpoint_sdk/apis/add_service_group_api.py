from aiohttp import ClientSession

from async_checkpoint_sdk.models.service_group_reply import ServiceGroupReply
from async_checkpoint_sdk.models.service_group_request_new import ServiceGroupRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_service_group(
    client: ClientSession, data: ServiceGroupRequestNew, config: SDKConfig, **kwargs
) -> ServiceGroupReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ServiceGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ServiceGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-service-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServiceGroupReply(**resp)
