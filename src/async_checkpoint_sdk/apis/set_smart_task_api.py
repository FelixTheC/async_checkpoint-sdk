from aiohttp import ClientSession

from async_checkpoint_sdk.models.smart_task_reply import SmartTaskReply
from async_checkpoint_sdk.models.smart_task_request_edit import SmartTaskRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_smart_task(
    client: ClientSession, data: SmartTaskRequestEdit, config: SDKConfig, **kwargs
) -> SmartTaskReply:
    """
    Edit existing object using object name or uid. <br>This command is available only in a Security Management environment or in Multi-Domain environment when logged into local domain.

    Parameters
    ----------
    client : ClientSession
    data : SmartTaskRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    SmartTaskReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-smart-task"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SmartTaskReply(**resp)
