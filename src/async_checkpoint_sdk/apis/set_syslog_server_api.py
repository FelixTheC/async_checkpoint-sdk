from aiohttp import ClientSession

from async_checkpoint_sdk.models.syslog_server_reply import SyslogServerReply
from async_checkpoint_sdk.models.syslog_server_request_edit import SyslogServerRequestEdit
from config import Config


async def set_syslog_server(
    client: ClientSession, data: SyslogServerRequestEdit, config: Config, **kwargs
) -> SyslogServerReply:
    """
    Edit existing syslog server using object name or uid.<br> Since syslog is not an encrypted protocol, Check Point highly recommends that the Security Gateway and the Log Proxy are located in proximity to each other and that they communicate over secure network.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SyslogServerRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SyslogServerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-syslog-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SyslogServerReply(**resp)
