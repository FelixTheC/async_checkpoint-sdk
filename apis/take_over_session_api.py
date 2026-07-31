from aiohttp import ClientSession

from config import Config
from models.work_session_reply import WorkSessionReply
from models.work_session_take_over_request import WorkSessionTakeOverRequest


async def take_over_session(
    client: ClientSession, data: WorkSessionTakeOverRequest, config: Config, **kwargs
) -> WorkSessionReply:
    """
    Take ownership of another session and start working on it.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WorkSessionTakeOverRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WorkSessionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/take-over-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WorkSessionReply(**resp)
