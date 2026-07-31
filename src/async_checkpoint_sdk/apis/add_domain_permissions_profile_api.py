from aiohttp import ClientSession

from async_checkpoint_sdk.models.domain_permissions_profile_reply import (
    DomainPermissionsProfileReply,
)
from async_checkpoint_sdk.models.domain_permissions_profile_request_new import (
    DomainPermissionsProfileRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_domain_permissions_profile(
    client: ClientSession, data: DomainPermissionsProfileRequestNew, config: SDKConfig, **kwargs
) -> DomainPermissionsProfileReply:
    """
    Create new Domain Permissions Profile.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DomainPermissionsProfileRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DomainPermissionsProfileReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-domain-permissions-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DomainPermissionsProfileReply(**resp)
