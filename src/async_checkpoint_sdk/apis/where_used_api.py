from aiohttp import ClientSession

from async_checkpoint_sdk.models.where_used_object_reply import WhereUsedObjectReply
from async_checkpoint_sdk.models.where_used_object_request import WhereUsedObjectRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def where_used(
    client: ClientSession, data: WhereUsedObjectRequest, config: SDKConfig, **kwargs
) -> WhereUsedObjectReply:
    """
    Searches for usage of the target object in other objects and rules.

    Parameters
    ----------
    client : ClientSession
    data : WhereUsedObjectRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    WhereUsedObjectReply

    """
    url = f"https://{config.server}:{config.port}/web_api/where-used"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WhereUsedObjectReply(**resp)
