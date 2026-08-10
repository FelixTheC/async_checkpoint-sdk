from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from async_checkpoint_sdk.models.object_in_group_with_members_query_request import (
    ObjectInGroupWithMembersQueryRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_unused_objects(
    client: ClientSession, data: ObjectInGroupWithMembersQueryRequest, config: SDKConfig, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all unused objects.

    Parameters
    ----------
    client : ClientSession
    data : ObjectInGroupWithMembersQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiQueryObjectReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-unused-objects"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
