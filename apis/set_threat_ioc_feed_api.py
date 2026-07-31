from config import Config
from aiohttp import ClientSession
from models.intelligence_feed_reply import IntelligenceFeedReply
from models.intelligence_feed_request_edit import IntelligenceFeedRequestEdit


async def set_threat_ioc_feed(
    client: ClientSession, data: IntelligenceFeedRequestEdit, config: Config, **kwargs
) -> IntelligenceFeedReply:
    """
    Edit an existing threat IOC feed.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : IntelligenceFeedRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
