from config import Config
from aiohttp import ClientSession
from models.time_request_edit import TimeRequestEdit
from models.time_reply import TimeReply


async def clone_time(
    client: ClientSession, data: TimeRequestEdit, config: Config, **kwargs
) -> TimeReply:
    """
    Clone existing object.
    
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
    url = f"https://{config.server}:{config.port}/web_api/clone-time"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TimeReply(**resp)
