from aiohttp import ClientSession

from async_checkpoint_sdk.models.time_reply import TimeReply
from async_checkpoint_sdk.models.time_request_edit import TimeRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_time(
    client: ClientSession, data: TimeRequestEdit, config: SDKConfig, **kwargs
) -> TimeReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TimeRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TimeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-time"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TimeReply(**resp)
