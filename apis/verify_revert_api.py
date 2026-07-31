from config import Config
from aiohttp import ClientSession
from models.verify_revert_request import VerifyRevertRequest
from models.api_task_reply import ApiTaskReply


async def verify_revert(
    client: ClientSession, data: VerifyRevertRequest, config: Config, **kwargs
) -> ApiTaskReply:
    """
    Verify the Management Database can revert to the selected revision.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : VerifyRevertRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/verify-revert"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
