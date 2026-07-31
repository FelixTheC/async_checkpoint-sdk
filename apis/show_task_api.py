from config import Config
from aiohttp import ClientSession
from models.task_reply import TaskReply
from models.task_request import TaskRequest


async def show_task(
    client: ClientSession, data: TaskRequest, config: Config, **kwargs
) -> TaskReply:
    """
    Show task progress and details.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TaskRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
