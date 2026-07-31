from aiohttp import ClientSession

from async_checkpoint_sdk.models.time_group_reply import TimeGroupReply
from async_checkpoint_sdk.models.time_group_request_edit import TimeGroupRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_time_group(
    client: ClientSession, data: TimeGroupRequestEdit, config: SDKConfig, **kwargs
) -> TimeGroupReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TimeGroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TimeGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-time-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TimeGroupReply(**resp)
