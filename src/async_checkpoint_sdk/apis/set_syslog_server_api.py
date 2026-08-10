from aiohttp import ClientSession

from async_checkpoint_sdk.models.syslog_server_reply import SyslogServerReply
from async_checkpoint_sdk.models.syslog_server_request_edit import SyslogServerRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_syslog_server(
    client: ClientSession, data: SyslogServerRequestEdit, config: SDKConfig, **kwargs
) -> SyslogServerReply:
    """
    Edit existing syslog server using object name or uid.<br> Since syslog is not an encrypted protocol, Check Point highly recommends that the Security Gateway and the Log Proxy are located in proximity to each other and that they communicate over secure network.

    Parameters
    ----------
    client : ClientSession
    data : SyslogServerRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
