from aiohttp import ClientSession

from async_checkpoint_sdk.models.syslog_server_reply import SyslogServerReply
from async_checkpoint_sdk.models.syslog_server_request_edit import SyslogServerRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_syslog_server(
    client: ClientSession, data: SyslogServerRequestEdit, config: SDKConfig, **kwargs
) -> SyslogServerReply:
    """
    Clone existing syslog server.

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
    url = f"https://{config.server}:{config.port}/web_api/clone-syslog-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SyslogServerReply(**resp)
