from aiohttp import ClientSession

from async_checkpoint_sdk.models.md_permissions_profile_reply import MdPermissionsProfileReply
from async_checkpoint_sdk.models.md_permissions_profile_request_edit import (
    MdPermissionsProfileRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_md_permissions_profile(
    client: ClientSession, data: MdPermissionsProfileRequestEdit, config: SDKConfig, **kwargs
) -> MdPermissionsProfileReply:
    """
    Edit existing Multi-Domain Permissions Profile using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : MdPermissionsProfileRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MdPermissionsProfileReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-md-permissions-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MdPermissionsProfileReply(**resp)
