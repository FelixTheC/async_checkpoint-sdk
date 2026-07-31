from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.work_session_purge_request import WorkSessionPurgeRequest
from config import Config


async def purge_published_sessions(
    client: ClientSession, data: WorkSessionPurgeRequest, config: Config, **kwargs
) -> ApiTaskReply:
    """
    Permanently deletes all data which belongs to the published sessions not selected for preservation. This operation is irreversible.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : WorkSessionPurgeRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    data : WorkSessionPurgeRequest [Argument]
        data : WorkSessionPurgeRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    data : WorkSessionPurgeRequest [Argument]
        data : WorkSessionPurgeRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    data : WorkSessionPurgeRequest [Argument]
        data : WorkSessionPurgeRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/purge-published-sessions"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
