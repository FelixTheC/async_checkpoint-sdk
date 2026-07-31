from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_message_reply import ApiMessageReply
from async_checkpoint_sdk.models.suppress_task_request import SuppressTaskRequest
from config import Config


async def suppress_task(
    client: ClientSession, data: SuppressTaskRequest, config: Config, **kwargs
) -> ApiMessageReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : SuppressTaskRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiMessageReply
    """
    url = f"https://{config.server}:{config.port}/web_api/suppress-task"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiMessageReply(**resp)
