from config import Config
from aiohttp import ClientSession
from models.empty_request import EmptyRequest
from models.playblocks_feeds_show_reply import PlayblocksFeedsShowReply


async def show_playblocks_feeds(
    client: ClientSession, data: EmptyRequest, config: Config, **kwargs
) -> PlayblocksFeedsShowReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : EmptyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PlayblocksFeedsShowReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-playblocks-feeds"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PlayblocksFeedsShowReply(**resp)
