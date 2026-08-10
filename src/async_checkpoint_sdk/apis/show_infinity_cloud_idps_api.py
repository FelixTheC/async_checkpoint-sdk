from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_request import ApiQueryRequest
from async_checkpoint_sdk.models.infinity_cloud_idp_query_reply import InfinityCloudIdpQueryReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_infinity_cloud_idps(
    client: ClientSession, data: ApiQueryRequest, config: SDKConfig, **kwargs
) -> InfinityCloudIdpQueryReply:
    """
    Retrieve all objects.

    Parameters
    ----------
    client : ClientSession
    data : ApiQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    InfinityCloudIdpQueryReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-infinity-cloud-idps"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InfinityCloudIdpQueryReply(**resp)
