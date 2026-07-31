from aiohttp import ClientSession

from async_checkpoint_sdk.models.idp_default_assignment_reply import IdpDefaultAssignmentReply
from async_checkpoint_sdk.models.idp_default_assignment_request_show import (
    IdpDefaultAssignmentRequestShow,
)
from config import Config


async def show_idp_default_assignment(
    client: ClientSession, data: IdpDefaultAssignmentRequestShow, config: Config, **kwargs
) -> IdpDefaultAssignmentReply:
    """
    Retrieve default Identity Provider assignment that used for Management server administrator access.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : IdpDefaultAssignmentRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IdpDefaultAssignmentReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-idp-default-assignment"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IdpDefaultAssignmentReply(**resp)
