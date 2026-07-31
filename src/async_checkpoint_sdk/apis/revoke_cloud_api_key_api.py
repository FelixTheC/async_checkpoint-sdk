from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.cloud_api_key_request import CloudApiKeyRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def revoke_cloud_api_key(
    client: ClientSession, data: CloudApiKeyRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CloudApiKeyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/revoke-cloud-api-key"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
