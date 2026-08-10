from aiohttp import ClientSession

from async_checkpoint_sdk.models.dynamic_global_network_reply import DynamicGlobalNetworkReply
from async_checkpoint_sdk.models.dynamic_global_network_request_edit import (
    DynamicGlobalNetworkRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_dynamic_global_network_object(
    client: ClientSession, data: DynamicGlobalNetworkRequestEdit, config: SDKConfig, **kwargs
) -> DynamicGlobalNetworkReply:
    """
    Edit existing object using object name or uid. <br>Local domain must have a corresponding network object (with the same name as the Dynamic Global Network Object) in order for Assignment to succeed.

    Parameters
    ----------
    client : ClientSession
    data : DynamicGlobalNetworkRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    DynamicGlobalNetworkReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-dynamic-global-network-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DynamicGlobalNetworkReply(**resp)
