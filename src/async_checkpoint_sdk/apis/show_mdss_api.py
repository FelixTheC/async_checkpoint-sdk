from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_object_reply import ApiQueryObjectReply
from async_checkpoint_sdk.models.mds_query_request import MdsQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_mdss(
    client: ClientSession, data: MdsQueryRequest, config: SDKConfig, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all objects of type Multi-Domain Server or Multi-Domain Log Server.

    Parameters
    ----------
    client : ClientSession
    data : MdsQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiQueryObjectReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-mdss"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
