from config import Config
from aiohttp import ClientSession
from models.package_info_command_reply import PackageInfoCommandReply
from models.package_info_command_request import PackageInfoCommandRequest


async def show_software_package_details(
    client: ClientSession, data: PackageInfoCommandRequest, config: Config, **kwargs
) -> PackageInfoCommandReply:
    """
    Gets the software package information from the cloud.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : PackageInfoCommandRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PackageInfoCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-software-package-details"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PackageInfoCommandReply(**resp)
