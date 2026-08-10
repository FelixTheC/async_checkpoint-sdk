from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.unsubscribe_object_request import UnsubscribeObjectRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def unsubscribe_objects(
    client: ClientSession, data: UnsubscribeObjectRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : UnsubscribeObjectRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiOkReply

    """
    url = f"https://{config.server}:{config.port}/web_api/unsubscribe-objects"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
