from aiohttp import ClientSession

from async_checkpoint_sdk.models.global_assignment_identifier_request import (
    GlobalAssignmentIdentifierRequest,
)
from async_checkpoint_sdk.models.global_assignment_reply import GlobalAssignmentReply
from config import Config


async def show_global_assignment(
    client: ClientSession, data: GlobalAssignmentIdentifierRequest, config: Config, **kwargs
) -> GlobalAssignmentReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : GlobalAssignmentIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GlobalAssignmentReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-global-assignment"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GlobalAssignmentReply(**resp)
