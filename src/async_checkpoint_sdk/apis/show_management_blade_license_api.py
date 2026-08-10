from aiohttp import ClientSession

from async_checkpoint_sdk.models.management_blade_license_reply import ManagementBladeLicenseReply
from async_checkpoint_sdk.models.management_blade_license_request_show import (
    ManagementBladeLicenseRequestShow,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_management_blade_license(
    client: ClientSession, data: ManagementBladeLicenseRequestShow, config: SDKConfig, **kwargs
) -> ManagementBladeLicenseReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : ManagementBladeLicenseRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ManagementBladeLicenseReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-management-blade-license"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ManagementBladeLicenseReply(**resp)
