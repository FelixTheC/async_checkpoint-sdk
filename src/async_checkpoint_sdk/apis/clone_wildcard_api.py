from aiohttp import ClientSession

from async_checkpoint_sdk.models.wildcard_reply import WildcardReply
from async_checkpoint_sdk.models.wildcard_request_edit import WildcardRequestEdit
from config import Config


async def clone_wildcard(
    client: ClientSession, data: WildcardRequestEdit, config: Config, **kwargs
) -> WildcardReply:
    """
    Clone existing object.

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
    url = f"https://{config.server}:{config.port}/web_api/clone-wildcard"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WildcardReply(**resp)
