from aiohttp import ClientSession

from config import Config
from models.threat_exception_reply import ThreatExceptionReply
from models.threat_exception_request_new import ThreatExceptionRequestNew


async def add_threat_exception(
    client: ClientSession, data: ThreatExceptionRequestNew, config: Config, **kwargs
) -> ThreatExceptionReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatExceptionRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatExceptionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-threat-exception"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatExceptionReply(**resp)
