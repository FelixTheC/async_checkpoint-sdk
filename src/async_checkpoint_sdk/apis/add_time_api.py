from aiohttp import ClientSession

from async_checkpoint_sdk.models.time_reply import TimeReply
from async_checkpoint_sdk.models.time_request_new import TimeRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_time(
    client: ClientSession, data: TimeRequestNew, config: SDKConfig, **kwargs
) -> TimeReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TimeRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TimeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-time"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TimeReply(**resp)
