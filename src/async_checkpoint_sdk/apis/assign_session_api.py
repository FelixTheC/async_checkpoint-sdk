from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.work_session_assign_request import WorkSessionAssignRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def assign_session(
    client: ClientSession, data: WorkSessionAssignRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Assign a session ownership to another administrator.

    Parameters
    ----------
    client : ClientSession
    data : WorkSessionAssignRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiOkReply

    """
    url = f"https://{config.server}:{config.port}/web_api/assign-session"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
