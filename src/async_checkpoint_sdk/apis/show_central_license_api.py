from aiohttp import ClientSession

from async_checkpoint_sdk.models.central_licenses_reply import CentralLicensesReply
from async_checkpoint_sdk.models.show_central_license_request import ShowCentralLicenseRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_central_license(
    client: ClientSession, data: ShowCentralLicenseRequest, config: SDKConfig, **kwargs
) -> CentralLicensesReply:
    """
    Show given license.

    Parameters
    ----------
    client : ClientSession
    data : ShowCentralLicenseRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    CentralLicensesReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-central-license"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CentralLicensesReply(**resp)
