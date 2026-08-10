from aiohttp import ClientSession

from async_checkpoint_sdk.models.threat_exception_group_reply import ThreatExceptionGroupReply
from async_checkpoint_sdk.models.threat_exception_group_request_edit import (
    ThreatExceptionGroupRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_exception_group(
    client: ClientSession, data: ThreatExceptionGroupRequestEdit, config: SDKConfig, **kwargs
) -> ThreatExceptionGroupReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ThreatExceptionGroupRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
