from aiohttp import ClientSession

from async_checkpoint_sdk.models.central_licenses_list_reply import CentralLicensesListReply
from async_checkpoint_sdk.models.delete_central_licenses_request import (
    DeleteCentralLicensesRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def delete_central_license(
    client: ClientSession, data: DeleteCentralLicensesRequest, config: SDKConfig, **kwargs
) -> CentralLicensesListReply:
    """
    Delete central license.

    Parameters
    ----------
    client : ClientSession
    data : DeleteCentralLicensesRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    CentralLicensesListReply

    """
    url = f"https://{config.server}:{config.port}/web_api/delete-central-license"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CentralLicensesListReply(**resp)
