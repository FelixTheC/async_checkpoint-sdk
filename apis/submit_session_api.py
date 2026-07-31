from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.workflow_submit_request import WorkflowSubmitRequest


async def submit_session(
    client: ClientSession, data: WorkflowSubmitRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Workflow feature - Submit the session for approval.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WorkflowSubmitRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/submit-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
