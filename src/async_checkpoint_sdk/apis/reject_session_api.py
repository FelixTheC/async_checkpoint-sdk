from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.workflow_reject_request import WorkflowRejectRequest
from config import Config


async def reject_session(
    client: ClientSession, data: WorkflowRejectRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Workflow feature - Return the session to the submitter administrator.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : WorkflowRejectRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/reject-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
