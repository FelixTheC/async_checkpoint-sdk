from aiohttp import ClientSession

from async_checkpoint_sdk.models.network_reply import NetworkReply
from async_checkpoint_sdk.models.network_request_new import NetworkRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_network(
    client: ClientSession, data: NetworkRequestNew, config: SDKConfig, **kwargs
) -> NetworkReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : NetworkRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NetworkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-network"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NetworkReply(**resp)
