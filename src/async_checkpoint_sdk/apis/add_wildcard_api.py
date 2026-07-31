from aiohttp import ClientSession

from async_checkpoint_sdk.models.wildcard_reply import WildcardReply
from async_checkpoint_sdk.models.wildcard_request_new import WildcardRequestNew
from config import Config


async def add_wildcard(
    client: ClientSession, data: WildcardRequestNew, config: Config, **kwargs
) -> WildcardReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : WildcardRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WildcardReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-wildcard"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WildcardReply(**resp)
