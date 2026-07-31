from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.work_session_object_identifier_request import WorkSessionObjectIdentifierRequest


async def continue_session_in_smartconsole(
    client: ClientSession, data: WorkSessionObjectIdentifierRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Logout from existing session. The session will be continued next time your open SmartConsole. In case 'uid' is not provided, use current session. In order for the session to pass successfully to SmartConsole, make sure you don't have any other active GUI sessions.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WorkSessionObjectIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
