from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.https_layer_reply import HttpsLayerReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_https_layer(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> HttpsLayerReply:
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
    HttpsLayerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-https-layer"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return HttpsLayerReply(**resp)
