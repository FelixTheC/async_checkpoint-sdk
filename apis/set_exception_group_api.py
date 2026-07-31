from aiohttp import ClientSession

from config import Config
from models.threat_exception_group_reply import ThreatExceptionGroupReply
from models.threat_exception_group_request_edit import ThreatExceptionGroupRequestEdit


async def set_exception_group(
    client: ClientSession, data: ThreatExceptionGroupRequestEdit, config: Config, **kwargs
) -> ThreatExceptionGroupReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatExceptionGroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatExceptionGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-exception-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatExceptionGroupReply(**resp)
