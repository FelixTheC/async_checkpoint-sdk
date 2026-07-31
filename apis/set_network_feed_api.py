from config import Config
from aiohttp import ClientSession
from models.network_feed_reply import NetworkFeedReply
from models.network_feed_request_edit import NetworkFeedRequestEdit


async def set_network_feed(
    client: ClientSession, data: NetworkFeedRequestEdit, config: Config, **kwargs
) -> NetworkFeedReply:
    """
    Edit an existing Network Feed.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : NetworkFeedRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NetworkFeedReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-network-feed"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NetworkFeedReply(**resp)
