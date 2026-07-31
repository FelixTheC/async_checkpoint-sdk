from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_message_reply import ApiMessageReply
from async_checkpoint_sdk.models.management_blade_trial_license_request import (
    ManagementBladeTrialLicenseRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def activate_management_blade_trial_license(
    client: ClientSession, data: ManagementBladeTrialLicenseRequest, config: SDKConfig, **kwargs
) -> ApiMessageReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ManagementBladeTrialLicenseRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiMessageReply
    """
    url = f"https://{config.server}:{config.port}/web_api/activate-management-blade-trial-license"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiMessageReply(**resp)
