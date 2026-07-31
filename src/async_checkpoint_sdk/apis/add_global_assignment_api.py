from aiohttp import ClientSession

from async_checkpoint_sdk.models.global_assignment_reply import GlobalAssignmentReply
from async_checkpoint_sdk.models.global_assignment_request_new import GlobalAssignmentRequestNew
from config import Config


async def add_global_assignment(
    client: ClientSession, data: GlobalAssignmentRequestNew, config: Config, **kwargs
) -> GlobalAssignmentReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GlobalAssignmentRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GlobalAssignmentReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-global-assignment"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GlobalAssignmentReply(**resp)
