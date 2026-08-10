from aiohttp import ClientSession

from async_checkpoint_sdk.models.domain_permissions_profile_reply import (
    DomainPermissionsProfileReply,
)
from async_checkpoint_sdk.models.domain_permissions_profile_request_edit import (
    DomainPermissionsProfileRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_domain_permissions_profile(
    client: ClientSession, data: DomainPermissionsProfileRequestEdit, config: SDKConfig, **kwargs
) -> DomainPermissionsProfileReply:
    """
    Edit existing Domain Permissions Profile using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : DomainPermissionsProfileRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    DomainPermissionsProfileReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-domain-permissions-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DomainPermissionsProfileReply(**resp)
