from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.workflow_approve_request import WorkflowApproveRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def approve_session(
    client: ClientSession, data: WorkflowApproveRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Workflow feature - Approve and Publish the session.

    Parameters
    ----------
    client : ClientSession
    data : WorkflowApproveRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
