from aiohttp import ClientSession

from async_checkpoint_sdk.models.task_query_reply import TaskQueryReply
from async_checkpoint_sdk.models.task_query_request import TaskQueryRequest
from config import Config


async def show_tasks(
    client: ClientSession, data: TaskQueryRequest, config: Config, **kwargs
) -> TaskQueryReply:
    """
    Retrieve all tasks and show their progress and details.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TaskQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TaskQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-tasks"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TaskQueryReply(**resp)
