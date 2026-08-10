from aiohttp import ClientSession

from async_checkpoint_sdk.models.dynamic_content_object_api_reply import (
    DynamicContentObjectApiReply,
)
from async_checkpoint_sdk.models.generic_object_identifier_request import (
    GenericObjectIdentifierRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_dynamic_content(
    client: ClientSession, data: GenericObjectIdentifierRequest, config: SDKConfig, **kwargs
) -> DynamicContentObjectApiReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : GenericObjectIdentifierRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    DynamicContentObjectApiReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-dynamic-content"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DynamicContentObjectApiReply(**resp)
