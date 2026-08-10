from aiohttp import ClientSession

from async_checkpoint_sdk.models.legacy_virtual_system_reply import LegacyVirtualSystemReply
from async_checkpoint_sdk.models.legacy_virtual_system_request_edit import (
    LegacyVirtualSystemRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_legacy_virtual_system(
    client: ClientSession, data: LegacyVirtualSystemRequestEdit, config: SDKConfig, **kwargs
) -> LegacyVirtualSystemReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : LegacyVirtualSystemRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LegacyVirtualSystemReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-legacy-virtual-system"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LegacyVirtualSystemReply(**resp)
