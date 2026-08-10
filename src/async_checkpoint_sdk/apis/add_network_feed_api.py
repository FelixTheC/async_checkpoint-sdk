from aiohttp import ClientSession

from async_checkpoint_sdk.models.network_feed_reply import NetworkFeedReply
from async_checkpoint_sdk.models.network_feed_request_new import NetworkFeedRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_network_feed(
    client: ClientSession, data: NetworkFeedRequestNew, config: SDKConfig, **kwargs
) -> NetworkFeedReply:
    """
    Create a new Network Feed.

    Parameters
    ----------
    client : ClientSession
    data : NetworkFeedRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    NetworkFeedReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-network-feed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NetworkFeedReply(**resp)
