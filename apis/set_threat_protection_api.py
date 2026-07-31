from config import Config
from aiohttp import ClientSession
from models.protection_request_edit import ProtectionRequestEdit
from models.protection_reply import ProtectionReply


async def set_threat_protection(
    client: ClientSession, data: ProtectionRequestEdit, config: Config, **kwargs
) -> ProtectionReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ProtectionRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ProtectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-threat-protection"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ProtectionReply(**resp)
