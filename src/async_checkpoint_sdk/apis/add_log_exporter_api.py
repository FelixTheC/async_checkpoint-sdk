from aiohttp import ClientSession

from async_checkpoint_sdk.models.log_exporter_reply import LogExporterReply
from async_checkpoint_sdk.models.log_exporter_request_new import LogExporterRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_log_exporter(
    client: ClientSession, data: LogExporterRequestNew, config: SDKConfig, **kwargs
) -> LogExporterReply:
    """
    Create new log exporter.<br>After you configure a Log Exporter, you must run Install Database.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LogExporterRequestNew [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogExporterReply
    config : Config [Argument]
        data : LogExporterRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogExporterReply
    config : Config [Argument]
        data : LogExporterRequestNew [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogExporterReply
    config : Config [Argument]
        data : LogExporterRequestNew [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LogExporterReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-log-exporter"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LogExporterReply(**resp)
