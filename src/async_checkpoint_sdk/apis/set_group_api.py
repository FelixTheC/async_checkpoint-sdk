from aiohttp import ClientSession

from async_checkpoint_sdk.models.group_reply import GroupReply
from async_checkpoint_sdk.models.group_request_edit import GroupRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_group(
    client: ClientSession, data: GroupRequestEdit, config: SDKConfig, **kwargs
) -> GroupReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GroupReply(**resp)
