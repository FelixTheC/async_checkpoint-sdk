from config import Config
from aiohttp import ClientSession
from models.smart_console_idle_timeout_reply import SmartConsoleIdleTimeoutReply
from models.smart_console_idle_timeout_request_show import SmartConsoleIdleTimeoutRequestShow


async def show_smart_console_idle_timeout(
    client: ClientSession, data: SmartConsoleIdleTimeoutRequestShow, config: Config, **kwargs
) -> SmartConsoleIdleTimeoutReply:
    """
    Retrieve existing SmartConsole idle timeout settings.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : SmartConsoleIdleTimeoutRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SmartConsoleIdleTimeoutReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-smart-console-idle-timeout"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SmartConsoleIdleTimeoutReply(**resp)
