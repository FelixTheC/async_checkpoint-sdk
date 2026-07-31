from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from async_checkpoint_sdk.models.group_with_exclusion_request_query import (
    GroupWithExclusionRequestQuery,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_groups_with_exclusion(
    client: ClientSession, data: GroupWithExclusionRequestQuery, config: SDKConfig, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all objects.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GroupWithExclusionRequestQuery [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-groups-with-exclusion"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
