from aiohttp import ClientSession

from async_checkpoint_sdk.models.protection_reply import ProtectionReply
from async_checkpoint_sdk.models.protection_request_show import ProtectionRequestShow
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_threat_protection(
    client: ClientSession, data: ProtectionRequestShow, config: SDKConfig, **kwargs
) -> ProtectionReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ProtectionRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ProtectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-threat-protection"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ProtectionReply(**resp)
