from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from async_checkpoint_sdk.models.radius_group_request_query import RadiusGroupRequestQuery
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_radius_groups(
    client: ClientSession, data: RadiusGroupRequestQuery, config: SDKConfig, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all objects.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : RadiusGroupRequestQuery [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-radius-groups"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
