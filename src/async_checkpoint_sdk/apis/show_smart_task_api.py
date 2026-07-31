from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.smart_task_reply import SmartTaskReply
from config import Config


async def show_smart_task(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> SmartTaskReply:
    """
    Retrieve existing object using object name or uid. <br>This command is available only in a Security Management environment or in Multi-Domain environment when logged into local domain.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SmartTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-smart-task"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SmartTaskReply(**resp)
