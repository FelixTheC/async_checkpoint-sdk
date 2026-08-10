from aiohttp import ClientSession

from async_checkpoint_sdk.models.md_permissions_profile_reply import MdPermissionsProfileReply
from async_checkpoint_sdk.models.md_permissions_profile_request_new import (
    MdPermissionsProfileRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_md_permissions_profile(
    client: ClientSession, data: MdPermissionsProfileRequestNew, config: SDKConfig, **kwargs
) -> MdPermissionsProfileReply:
    """
    Create new Multi-Domain Permissions Profile.

    Parameters
    ----------
    client : ClientSession
    data : MdPermissionsProfileRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MdPermissionsProfileReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-md-permissions-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MdPermissionsProfileReply(**resp)
