from aiohttp import ClientSession

from async_checkpoint_sdk.models.import_smart_task_api_request import ImportSmartTaskApiRequest
from async_checkpoint_sdk.models.import_smart_task_reply import ImportSmartTaskReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def import_smart_task(
    client: ClientSession, data: ImportSmartTaskApiRequest, config: SDKConfig, **kwargs
) -> ImportSmartTaskReply:
    """
    Import SmartTask from a file. <br>This command is available only in a Security Management environment or in Multi-Domain environment when logged into local domain.

    Parameters
    ----------
    client : ClientSession
    data : ImportSmartTaskApiRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ImportSmartTaskReply

    """
    url = f"https://{config.server}:{config.port}/web_api/import-smart-task"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ImportSmartTaskReply(**resp)
