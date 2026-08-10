from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.security_zone_reply import SecurityZoneReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_security_zone(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> SecurityZoneReply:
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
    SecurityZoneReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-security-zone"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecurityZoneReply(**resp)
