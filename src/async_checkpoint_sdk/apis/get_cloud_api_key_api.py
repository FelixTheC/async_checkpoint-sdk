from aiohttp import ClientSession

from async_checkpoint_sdk.models.cloud_api_key_request import CloudApiKeyRequest
from async_checkpoint_sdk.models.get_cloud_api_key_reply import GetCloudApiKeyReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def get_cloud_api_key(
    client: ClientSession, data: CloudApiKeyRequest, config: SDKConfig, **kwargs
) -> GetCloudApiKeyReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CloudApiKeyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GetCloudApiKeyReply
    """
    url = f"https://{config.server}:{config.port}/web_api/get-cloud-api-key"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GetCloudApiKeyReply(**resp)
