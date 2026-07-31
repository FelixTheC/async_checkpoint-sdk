from config import Config
from aiohttp import ClientSession
from models.distribute_licenses_reply import DistributeLicensesReply
from models.distribute_cloud_guard_licenses_request import DistributeCloudGuardLicensesRequest


async def distribute_cloud_licenses(
    client: ClientSession, data: DistributeCloudGuardLicensesRequest, config: Config, **kwargs
) -> DistributeLicensesReply:
    """
    Distribute licenses to target CloudGuard gateways. For more information, see the <A HREF = "https://sc1.checkpoint.com/documents/IaaS/WebAdminGuides/EN/CP_CloudGuard_Central_License_Tool_Admin_Guide/Content/Topics-Central-License-Tool/Overview.htm?tocpath=Overview%7C_____0#Overview"><b>Central License Administration Guide</b></A>.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : DistributeCloudGuardLicensesRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DistributeLicensesReply
    """
    url = f"https://{config.server}:{config.port}/web_api/distribute-cloud-licenses"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DistributeLicensesReply(**resp)
