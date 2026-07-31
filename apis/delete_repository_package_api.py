from config import Config
from aiohttp import ClientSession
from models.delete_package_command_request import DeletePackageCommandRequest
from models.delete_package_command_reply import DeletePackageCommandReply


async def delete_repository_package(
    client: ClientSession, data: DeletePackageCommandRequest, config: Config, **kwargs
) -> DeletePackageCommandReply:
    """
    Delete the repository software package from the central repository.<br>On a Multi-Domain Server, you must connect to the relevant Domain.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : DeletePackageCommandRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DeletePackageCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-repository-package"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DeletePackageCommandReply(**resp)
