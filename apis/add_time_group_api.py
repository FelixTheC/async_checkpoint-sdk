from aiohttp import ClientSession

from config import Config
from models.time_group_reply import TimeGroupReply
from models.time_group_request_new import TimeGroupRequestNew


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
