from aiohttp import ClientSession

from async_checkpoint_sdk.models.task_reply import TaskReply
from async_checkpoint_sdk.models.task_request import TaskRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_task(
    client: ClientSession, data: TaskRequest, config: SDKConfig, **kwargs
) -> TaskReply:
    """
    Show task progress and details.

    Parameters
    ----------
    client : ClientSession
    data : TaskRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TaskReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-task"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TaskReply(**resp)
