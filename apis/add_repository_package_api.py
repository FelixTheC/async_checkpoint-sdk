from aiohttp import ClientSession

from config import Config
from models.add_package_command_reply import AddPackageCommandReply
from models.add_package_command_request import AddPackageCommandRequest


async def add_repository_package(
    client: ClientSession, data: AddPackageCommandRequest, config: Config, **kwargs
) -> AddPackageCommandReply:
    """
    Add the software package to the central repository.<br>On Multi-Domain Server this command is available only after logging in to the Global domain.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AddPackageCommandRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AddPackageCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-repository-package"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AddPackageCommandReply(**resp)
