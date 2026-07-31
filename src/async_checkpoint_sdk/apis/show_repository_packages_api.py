from aiohttp import ClientSession

from async_checkpoint_sdk.models.packages_info_command_reply import PackagesInfoCommandReply
from async_checkpoint_sdk.models.packages_info_command_request import PackagesInfoCommandRequest
from config import Config


async def show_repository_packages(
    client: ClientSession, data: PackagesInfoCommandRequest, config: Config, **kwargs
) -> PackagesInfoCommandReply:
    """
    Gets all repository software packages information.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : PackagesInfoCommandRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PackagesInfoCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-repository-packages"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PackagesInfoCommandReply(**resp)
