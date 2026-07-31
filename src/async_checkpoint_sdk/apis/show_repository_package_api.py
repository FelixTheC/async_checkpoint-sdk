from aiohttp import ClientSession

from async_checkpoint_sdk.models.package_info_command_reply import PackageInfoCommandReply
from async_checkpoint_sdk.models.package_info_command_request import PackageInfoCommandRequest
from config import Config


async def show_repository_package(
    client: ClientSession, data: PackageInfoCommandRequest, config: Config, **kwargs
) -> PackageInfoCommandReply:
    """
    Gets repository software packages information.

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
    url = f"https://{config.server}:{config.port}/web_api/show-repository-package"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PackageInfoCommandReply(**resp)
