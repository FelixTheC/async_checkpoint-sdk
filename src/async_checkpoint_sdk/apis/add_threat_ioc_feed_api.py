from aiohttp import ClientSession

from async_checkpoint_sdk.models.intelligence_feed_reply import IntelligenceFeedReply
from async_checkpoint_sdk.models.intelligence_feed_request_new import IntelligenceFeedRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_threat_ioc_feed(
    client: ClientSession, data: IntelligenceFeedRequestNew, config: SDKConfig, **kwargs
) -> IntelligenceFeedReply:
    """
    Create a new threat IOC feed.

    Parameters
    ----------
    client : ClientSession
    data : IntelligenceFeedRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    IntelligenceFeedReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-threat-ioc-feed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IntelligenceFeedReply(**resp)
