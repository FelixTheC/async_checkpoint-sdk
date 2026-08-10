from aiohttp import ClientSession

from async_checkpoint_sdk.models.sho_reply import ShoReply
from async_checkpoint_sdk.models.sho_request import ShoRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def configuration_sharing(
    client: ClientSession, data: ShoRequest, config: SDKConfig, **kwargs
) -> ShoReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : ShoRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ShoReply

    """
    url = f"https://{config.server}:{config.port}/web_api/configuration-sharing"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShoReply(**resp)
