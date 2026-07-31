from aiohttp import ClientSession

from config import Config
from models.intelligence_feed_reply import IntelligenceFeedReply
from models.intelligence_feed_request_new import IntelligenceFeedRequestNew


async def add_threat_ioc_feed(
    client: ClientSession, data: IntelligenceFeedRequestNew, config: Config, **kwargs
) -> IntelligenceFeedReply:
    """
    Create a new threat IOC feed.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : IntelligenceFeedRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
