from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.intelligence_feed_reply import IntelligenceFeedReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_threat_ioc_feed(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> IntelligenceFeedReply:
    """
    Displays a threat IOC feed.

    Parameters
    ----------
    client : ClientSession
    data : ApiVisualCPObjectIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    IntelligenceFeedReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-threat-ioc-feed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IntelligenceFeedReply(**resp)
