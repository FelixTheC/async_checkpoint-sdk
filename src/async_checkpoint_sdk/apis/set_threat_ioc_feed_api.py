from aiohttp import ClientSession

from async_checkpoint_sdk.models.intelligence_feed_reply import IntelligenceFeedReply
from async_checkpoint_sdk.models.intelligence_feed_request_edit import IntelligenceFeedRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_threat_ioc_feed(
    client: ClientSession, data: IntelligenceFeedRequestEdit, config: SDKConfig, **kwargs
) -> IntelligenceFeedReply:
    """
    Edit an existing threat IOC feed.

    Parameters
    ----------
    client : ClientSession
    data : IntelligenceFeedRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    IntelligenceFeedReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-threat-ioc-feed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IntelligenceFeedReply(**resp)
