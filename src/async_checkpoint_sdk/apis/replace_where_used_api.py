from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.where_used_replace_object_request import (
    WhereUsedReplaceObjectRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def replace_where_used(
    client: ClientSession, data: WhereUsedReplaceObjectRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Replaces all references to an object with a new object according to specified criteria.

    Parameters
    ----------
    client : ClientSession
    data : WhereUsedReplaceObjectRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiOkReply

    """
    url = f"https://{config.server}:{config.port}/web_api/replace-where-used"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
