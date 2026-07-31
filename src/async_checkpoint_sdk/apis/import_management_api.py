from aiohttp import ClientSession

from async_checkpoint_sdk.models.upgrade_import_reply import UpgradeImportReply
from async_checkpoint_sdk.models.upgrade_import_request import UpgradeImportRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def import_management(
    client: ClientSession, data: UpgradeImportRequest, config: SDKConfig, **kwargs
) -> UpgradeImportReply:
    """
    Import the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration. <br/>After the import starts, the session expires and you must login again.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : UpgradeImportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpgradeImportReply
    data : UpgradeImportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
        data : UpgradeImportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpgradeImportReply
    data : UpgradeImportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
        data : UpgradeImportRequest [Argument]
        database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UpgradeImportReply
    """
    url = f"https://{config.server}:{config.port}/web_api/import-management"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UpgradeImportReply(**resp)
