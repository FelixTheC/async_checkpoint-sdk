from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.workflow_approve_request import WorkflowApproveRequest


async def approve_session(
    client: ClientSession, data: WorkflowApproveRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Workflow feature - Approve and Publish the session.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WorkflowApproveRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/approve-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
