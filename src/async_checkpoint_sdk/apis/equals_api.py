from aiohttp import ClientSession

from async_checkpoint_sdk.models.equals_reply import EqualsReply
from async_checkpoint_sdk.models.equals_request import EqualsRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def equals(
    client: ClientSession, data: EqualsRequest, config: SDKConfig, **kwargs
) -> EqualsReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : EqualsRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    EqualsReply

    """
    url = f"https://{config.server}:{config.port}/web_api/equals"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return EqualsReply(**resp)
