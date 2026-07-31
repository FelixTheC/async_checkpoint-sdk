from aiohttp import ClientSession

from async_checkpoint_sdk.models.smart_task_reply import SmartTaskReply
from async_checkpoint_sdk.models.smart_task_request_new import SmartTaskRequestNew
from config import Config


async def add_smart_task(
    client: ClientSession, data: SmartTaskRequestNew, config: Config, **kwargs
) -> SmartTaskReply:
    """
    Create a new Smart Task. <br>This command is available only in a Security Management environment or in Multi-Domain environment when logged into local domain.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SmartTaskRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SmartTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-smart-task"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SmartTaskReply(**resp)
