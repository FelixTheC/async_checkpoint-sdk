from aiohttp import ClientSession

from async_checkpoint_sdk.models.log_exporter_reply import LogExporterReply
from async_checkpoint_sdk.models.log_exporter_request_edit import LogExporterRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_log_exporter(
    client: ClientSession, data: LogExporterRequestEdit, config: SDKConfig, **kwargs
) -> LogExporterReply:
    """
    Clone existing log exporter.

    Parameters
    ----------
    client : ClientSession
    data : LogExporterRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LogExporterReply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-log-exporter"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LogExporterReply(**resp)
