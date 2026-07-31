from aiohttp import ClientSession

from async_checkpoint_sdk.models.compliance_scan_reply import ComplianceScanReply
from async_checkpoint_sdk.models.compliance_scan_request import ComplianceScanRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def compliance_scan(
    client: ClientSession, data: ComplianceScanRequest, config: SDKConfig, **kwargs
) -> ComplianceScanReply:
    """
       Runs the Compliance Software Blade scan. The scan evaluates the configuration compliance with the relevant best practices.
    Important note - This API only triggers the scan. You can see the scan report only in SmartConsole.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ComplianceScanRequest [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ComplianceScanReply
    config : Config [Argument]
        data : ComplianceScanRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ComplianceScanReply
    config : Config [Argument]
        data : ComplianceScanRequest [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ComplianceScanReply
    """
    url = f"https://{config.server}:{config.port}/web_api/compliance-scan"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ComplianceScanReply(**resp)
