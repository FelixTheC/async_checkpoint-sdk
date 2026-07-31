from aiohttp import ClientSession

from async_checkpoint_sdk.models.security_zone_reply import SecurityZoneReply
from async_checkpoint_sdk.models.security_zone_request_edit import SecurityZoneRequestEdit
from config import Config


async def set_security_zone(
    client: ClientSession, data: SecurityZoneRequestEdit, config: Config, **kwargs
) -> SecurityZoneReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SecurityZoneRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SecurityZoneReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-security-zone"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecurityZoneReply(**resp)
