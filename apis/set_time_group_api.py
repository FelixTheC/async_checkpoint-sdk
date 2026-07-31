from config import Config
from aiohttp import ClientSession
from models.time_group_request_edit import TimeGroupRequestEdit
from models.time_group_reply import TimeGroupReply


async def set_time_group(
    client: ClientSession, data: TimeGroupRequestEdit, config: Config, **kwargs
) -> TimeGroupReply:
    """
    Edit existing object using object name or uid.
    
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
    url = f"https://{config.server}:{config.port}/web_api/set-time-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TimeGroupReply(**resp)
