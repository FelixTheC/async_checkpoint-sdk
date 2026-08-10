from aiohttp import ClientSession

from async_checkpoint_sdk.models.diff_reply_task import DiffReplyTask
from async_checkpoint_sdk.models.diff_request import DiffRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_changes(
    client: ClientSession, data: DiffRequest, config: SDKConfig, **kwargs
) -> DiffReplyTask:
    """
    Show changes between two sessions.

    Parameters
    ----------
    client : ClientSession
    data : DiffRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    DiffReplyTask

    """
    url = f"https://{config.server}:{config.port}/web_api/show-changes"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DiffReplyTask(**resp)
