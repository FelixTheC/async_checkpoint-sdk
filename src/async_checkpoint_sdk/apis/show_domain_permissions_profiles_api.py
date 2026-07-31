from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from async_checkpoint_sdk.models.domain_permissions_profile_query_request import (
    DomainPermissionsProfileQueryRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_domain_permissions_profiles(
    client: ClientSession, data: DomainPermissionsProfileQueryRequest, config: SDKConfig, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all Domain Permissions Profiles.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DomainPermissionsProfileQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-domain-permissions-profiles"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
