from aiohttp import ClientSession

from async_checkpoint_sdk.models.view_central_licenses_list_reply import (
    ViewCentralLicensesListReply,
)
from async_checkpoint_sdk.models.view_central_licenses_request import ViewCentralLicensesRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_cloud_licenses_usage(
    client: ClientSession, data: ViewCentralLicensesRequest, config: SDKConfig, **kwargs
) -> ViewCentralLicensesListReply:
    """
    Show attached licenses usage.

    Parameters
    ----------
    client : ClientSession
    data : ViewCentralLicensesRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ViewCentralLicensesListReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-cloud-licenses-usage"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ViewCentralLicensesListReply(**resp)
