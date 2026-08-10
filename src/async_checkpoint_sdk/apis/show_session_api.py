from aiohttp import ClientSession

from async_checkpoint_sdk.models.work_session_request_show import WorkSessionRequestShow
from async_checkpoint_sdk.models.work_session_show_reply import WorkSessionShowReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_session(
    client: ClientSession, data: WorkSessionRequestShow, config: SDKConfig, **kwargs
) -> WorkSessionShowReply:
    """
    Show session.

    Parameters
    ----------
    client : ClientSession
    data : WorkSessionRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
