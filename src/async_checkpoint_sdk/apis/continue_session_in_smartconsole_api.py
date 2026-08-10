from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.work_session_object_identifier_request import (
    WorkSessionObjectIdentifierRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def continue_session_in_smartconsole(
    client: ClientSession, data: WorkSessionObjectIdentifierRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Logout from existing session. The session will be continued next time your open SmartConsole. In case 'uid' is not provided, use current session. In order for the session to pass successfully to SmartConsole, make sure you don't have any other active GUI sessions.

    Parameters
    ----------
    client : ClientSession
    data : WorkSessionObjectIdentifierRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiOkReply

    """
    url = f"https://{config.server}:{config.port}/web_api/continue-session-in-smartconsole"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
