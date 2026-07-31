from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.dynamic_global_network_reply import DynamicGlobalNetworkReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_dynamic_global_network_object(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> DynamicGlobalNetworkReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DynamicGlobalNetworkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-dynamic-global-network-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DynamicGlobalNetworkReply(**resp)
