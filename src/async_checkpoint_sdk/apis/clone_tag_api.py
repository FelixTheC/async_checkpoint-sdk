from aiohttp import ClientSession

from async_checkpoint_sdk.models.tag_reply import TagReply
from async_checkpoint_sdk.models.tag_request_edit import TagRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_tag(
    client: ClientSession, data: TagRequestEdit, config: SDKConfig, **kwargs
) -> TagReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : TagRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TagReply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-tag"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TagReply(**resp)
