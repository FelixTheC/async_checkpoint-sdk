from aiohttp import ClientSession

from async_checkpoint_sdk.models.upgrade_export_reply import UpgradeExportReply
from async_checkpoint_sdk.models.upgrade_export_request import UpgradeExportRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def export_management(
    client: ClientSession, data: UpgradeExportRequest, config: SDKConfig, **kwargs
) -> UpgradeExportReply:
    """
    Export the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration.

    Parameters
    ----------
    client : ClientSession
        data : UpgradeExportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpgradeExportReply
    data : UpgradeExportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
        data : UpgradeExportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpgradeExportReply
    data : UpgradeExportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
        data : UpgradeExportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpgradeExportReply.
    data : UpgradeExportRequest
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point.
    config : SDKConfig
        data : UpgradeExportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument].
    kwargs : Any
        Keyword arguments

    Returns
    -------
    UpgradeExportReply

    """
    url = f"https://{config.server}:{config.port}/web_api/export-management"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UpgradeExportReply(**resp)
