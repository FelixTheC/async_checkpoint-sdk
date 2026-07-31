from aiohttp import ClientSession

from async_checkpoint_sdk.models.threat_exception_group_reply import ThreatExceptionGroupReply
from async_checkpoint_sdk.models.threat_exception_group_request_new import (
    ThreatExceptionGroupRequestNew,
)
from config import Config


async def add_exception_group(
    client: ClientSession, data: ThreatExceptionGroupRequestNew, config: Config, **kwargs
) -> ThreatExceptionGroupReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatExceptionGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatExceptionGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-exception-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatExceptionGroupReply(**resp)
