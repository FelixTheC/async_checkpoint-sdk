from config import Config
from aiohttp import ClientSession
from models.management_blade_license_request_show import ManagementBladeLicenseRequestShow
from models.management_blade_license_reply import ManagementBladeLicenseReply


async def show_management_blade_license(
    client: ClientSession, data: ManagementBladeLicenseRequestShow, config: Config, **kwargs
) -> ManagementBladeLicenseReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ManagementBladeLicenseRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
