from aiohttp import ClientSession

from async_checkpoint_sdk.models.work_session_request_show import WorkSessionRequestShow
from async_checkpoint_sdk.models.work_session_show_reply import WorkSessionShowReply
from config import Config


async def show_session(
    client: ClientSession, data: WorkSessionRequestShow, config: Config, **kwargs
) -> WorkSessionShowReply:
    """
    Show session.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : WorkSessionRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WorkSessionShowReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WorkSessionShowReply(**resp)
