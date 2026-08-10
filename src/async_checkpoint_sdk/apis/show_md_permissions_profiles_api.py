from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from async_checkpoint_sdk.models.md_permissions_profile_query_request import (
    MdPermissionsProfileQueryRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_md_permissions_profiles(
    client: ClientSession, data: MdPermissionsProfileQueryRequest, config: SDKConfig, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all Multi-Domain Permissions Profiles.

    Parameters
    ----------
    client : ClientSession
    data : MdPermissionsProfileQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiQueryObjectReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-md-permissions-profiles"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
