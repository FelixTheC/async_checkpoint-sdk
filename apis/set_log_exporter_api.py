from aiohttp import ClientSession

from config import Config
from models.log_exporter_reply import LogExporterReply
from models.log_exporter_request_edit import LogExporterRequestEdit


async def set_log_exporter(
    client: ClientSession, data: LogExporterRequestEdit, config: Config, **kwargs
) -> LogExporterReply:
    """
    Edit existing log exporter using object name or uid.<br>After you configure a Log Exporter, you must run Install Database.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : LogExporterRequestEdit [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogExporterReply
    config : Config [Argument]
        data : LogExporterRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogExporterReply
    config : Config [Argument]
        data : LogExporterRequestEdit [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogExporterReply
    config : Config [Argument]
        data : LogExporterRequestEdit [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogExporterReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-log-exporter"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LogExporterReply(**resp)
