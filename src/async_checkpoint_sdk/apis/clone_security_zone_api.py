from aiohttp import ClientSession

from async_checkpoint_sdk.models.security_zone_reply import SecurityZoneReply
from async_checkpoint_sdk.models.security_zone_request_edit import SecurityZoneRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_security_zone(
    client: ClientSession, data: SecurityZoneRequestEdit, config: SDKConfig, **kwargs
) -> SecurityZoneReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : SecurityZoneRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    SecurityZoneReply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-security-zone"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecurityZoneReply(**resp)
