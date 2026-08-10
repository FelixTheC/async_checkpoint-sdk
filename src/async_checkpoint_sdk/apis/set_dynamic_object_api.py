from aiohttp import ClientSession

from async_checkpoint_sdk.models.dynamic_object_reply import DynamicObjectReply
from async_checkpoint_sdk.models.dynamic_object_request_edit import DynamicObjectRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_dynamic_object(
    client: ClientSession, data: DynamicObjectRequestEdit, config: SDKConfig, **kwargs
) -> DynamicObjectReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : DynamicObjectRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    DynamicObjectReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-dynamic-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DynamicObjectReply(**resp)
