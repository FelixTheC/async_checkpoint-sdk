from aiohttp import ClientSession

from async_checkpoint_sdk.models.time_group_reply import TimeGroupReply
from async_checkpoint_sdk.models.time_group_request_new import TimeGroupRequestNew
from config import Config


async def add_time_group(
    client: ClientSession, data: TimeGroupRequestNew, config: Config, **kwargs
) -> TimeGroupReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TimeGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TimeGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-time-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TimeGroupReply(**resp)
