from aiohttp import ClientSession

from async_checkpoint_sdk.models.global_assignment_reply import GlobalAssignmentReply
from async_checkpoint_sdk.models.global_assignment_request_edit import GlobalAssignmentRequestEdit
from config import Config


async def set_global_assignment(
    client: ClientSession, data: GlobalAssignmentRequestEdit, config: Config, **kwargs
) -> GlobalAssignmentReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GlobalAssignmentRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GlobalAssignmentReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-global-assignment"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GlobalAssignmentReply(**resp)
