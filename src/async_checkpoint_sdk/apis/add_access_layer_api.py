from aiohttp import ClientSession

from async_checkpoint_sdk.models.access_layer_reply import AccessLayerReply
from async_checkpoint_sdk.models.access_layer_request_new import AccessLayerRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_access_layer(
    client: ClientSession, data: AccessLayerRequestNew, config: SDKConfig, **kwargs
) -> AccessLayerReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : AccessLayerRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    AccessLayerReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-access-layer"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessLayerReply(**resp)
