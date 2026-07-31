from aiohttp import ClientSession

from async_checkpoint_sdk.models.tag_reply import TagReply
from async_checkpoint_sdk.models.tag_request_edit import TagRequestEdit
from config import Config


async def set_tag(
    client: ClientSession, data: TagRequestEdit, config: Config, **kwargs
) -> TagReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TagRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TagReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-tag"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TagReply(**resp)
