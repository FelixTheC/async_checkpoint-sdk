from aiohttp import ClientSession

from config import Config
from models.management_blade_trial_license_request import ManagementBladeTrialLicenseRequest
from models.management_blade_trial_license_show_reply import ManagementBladeTrialLicenseShowReply


async def show_management_blade_trial_license(
    client: ClientSession, data: ManagementBladeTrialLicenseRequest, config: Config, **kwargs
) -> ManagementBladeTrialLicenseShowReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ManagementBladeTrialLicenseRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ManagementBladeTrialLicenseShowReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-management-blade-trial-license"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ManagementBladeTrialLicenseShowReply(**resp)
