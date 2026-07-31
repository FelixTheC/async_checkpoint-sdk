from aiohttp import ClientSession

from async_checkpoint_sdk.models.access_layers_query_reply import AccessLayersQueryReply
from async_checkpoint_sdk.models.api_query_request import ApiQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_access_layers(
    client: ClientSession, data: ApiQueryRequest, config: SDKConfig, **kwargs
) -> AccessLayersQueryReply:
    """
    Retrieve all objects.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AccessLayersQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-access-layers"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessLayersQueryReply(**resp)
