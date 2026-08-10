from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.service_icmp_reply import ServiceIcmpReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_service_icmp(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> ServiceIcmpReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ApiVisualCPObjectIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ServiceIcmpReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-service-icmp"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServiceIcmpReply(**resp)
