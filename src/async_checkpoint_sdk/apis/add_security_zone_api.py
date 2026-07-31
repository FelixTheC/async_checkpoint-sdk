from aiohttp import ClientSession

from async_checkpoint_sdk.models.security_zone_reply import SecurityZoneReply
from async_checkpoint_sdk.models.security_zone_request_new import SecurityZoneRequestNew
from config import Config


async def add_security_zone(
    client: ClientSession, data: SecurityZoneRequestNew, config: Config, **kwargs
) -> SecurityZoneReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SecurityZoneRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SecurityZoneReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-security-zone"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecurityZoneReply(**resp)
