from aiohttp import ClientSession

from async_checkpoint_sdk.models.dynamic_global_network_reply import DynamicGlobalNetworkReply
from async_checkpoint_sdk.models.dynamic_global_network_request_new import (
    DynamicGlobalNetworkRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_dynamic_global_network_object(
    client: ClientSession, data: DynamicGlobalNetworkRequestNew, config: SDKConfig, **kwargs
) -> DynamicGlobalNetworkReply:
    """
    Create new object. <br>Local domain must have a corresponding network object (with the same name as the Dynamic Global Network Object) in order for Assignment to succeed.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DynamicGlobalNetworkRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DynamicGlobalNetworkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-dynamic-global-network-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DynamicGlobalNetworkReply(**resp)
