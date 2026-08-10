from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from async_checkpoint_sdk.models.idp_group_query_request import IdpGroupQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_idp_administrator_groups(
    client: ClientSession, data: IdpGroupQueryRequest, config: SDKConfig, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all Identity Provider administrators groups.

    Parameters
    ----------
    client : ClientSession
    data : IdpGroupQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiQueryObjectReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-idp-administrator-groups"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
