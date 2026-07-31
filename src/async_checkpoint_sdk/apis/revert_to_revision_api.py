from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.revert_to_revision_request import RevertToRevisionRequest
from config import Config


async def revert_to_revision(
    client: ClientSession, data: RevertToRevisionRequest, config: Config, **kwargs
) -> ApiTaskReply:
    """
    Revert the Management Database to the selected revision.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : RevertToRevisionRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/revert-to-revision"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
