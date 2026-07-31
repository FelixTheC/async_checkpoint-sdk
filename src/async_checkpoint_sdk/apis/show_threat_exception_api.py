from aiohttp import ClientSession

from async_checkpoint_sdk.models.threat_exception_identifier_request import (
    ThreatExceptionIdentifierRequest,
)
from async_checkpoint_sdk.models.threat_exception_reply import ThreatExceptionReply
from config import Config


async def show_threat_exception(
    client: ClientSession, data: ThreatExceptionIdentifierRequest, config: Config, **kwargs
) -> ThreatExceptionReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatExceptionIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatExceptionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-threat-exception"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatExceptionReply(**resp)
