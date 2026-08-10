from aiohttp import ClientSession

from async_checkpoint_sdk.models.add_api_key_reply import AddApiKeyReply
from async_checkpoint_sdk.models.api_key_request import ApiKeyRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_api_key(
    client: ClientSession, data: ApiKeyRequest, config: SDKConfig, **kwargs
) -> AddApiKeyReply:
    """
    Add API key for administrator, to enable login with it. For the key to be valid publish is needed. <br>When using mgmt_cli tool, add -f json to get the key in the command's output.

    Parameters
    ----------
    client : ClientSession
    data : ApiKeyRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    AddApiKeyReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-api-key"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AddApiKeyReply(**resp)
