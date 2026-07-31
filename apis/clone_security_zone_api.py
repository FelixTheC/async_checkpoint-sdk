from config import Config
from aiohttp import ClientSession
from models.security_zone_reply import SecurityZoneReply
from models.security_zone_request_edit import SecurityZoneRequestEdit


async def clone_security_zone(
    client: ClientSession, data: SecurityZoneRequestEdit, config: Config, **kwargs
) -> SecurityZoneReply:
    """
    Clone existing object.
    
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
    url = f"https://{config.server}:{config.port}/web_api/clone-security-zone"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecurityZoneReply(**resp)
