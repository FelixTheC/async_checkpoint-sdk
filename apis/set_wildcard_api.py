from config import Config
from aiohttp import ClientSession
from models.wildcard_reply import WildcardReply
from models.wildcard_request_edit import WildcardRequestEdit


async def set_wildcard(
    client: ClientSession, data: WildcardRequestEdit, config: Config, **kwargs
) -> WildcardReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WildcardRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WildcardReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-wildcard"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WildcardReply(**resp)
