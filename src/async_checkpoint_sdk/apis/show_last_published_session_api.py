from aiohttp import ClientSession

from async_checkpoint_sdk.models.empty_request import EmptyRequest
from async_checkpoint_sdk.models.work_session_reply import WorkSessionReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_last_published_session(
    client: ClientSession, data: EmptyRequest, config: SDKConfig, **kwargs
) -> WorkSessionReply:
    """
    Shows the last published session.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : EmptyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WorkSessionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-last-published-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WorkSessionReply(**resp)
