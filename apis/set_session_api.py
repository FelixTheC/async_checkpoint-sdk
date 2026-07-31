from config import Config
from aiohttp import ClientSession
from models.work_session_request_edit import WorkSessionRequestEdit
from models.work_session_reply import WorkSessionReply


async def set_session(
    client: ClientSession, data: WorkSessionRequestEdit, config: Config, **kwargs
) -> WorkSessionReply:
    """
    Edit user's current session.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WorkSessionRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WorkSessionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WorkSessionReply(**resp)
