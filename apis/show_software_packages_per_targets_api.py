from config import Config
from aiohttp import ClientSession
from models.packages_per_target_command_reply import PackagesPerTargetCommandReply
from models.packages_per_target_command_request import PackagesPerTargetCommandRequest


async def show_software_packages_per_targets(
    client: ClientSession, data: PackagesPerTargetCommandRequest, config: Config, **kwargs
) -> PackagesPerTargetCommandReply:
    """
    Shows software packages on targets.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : PackagesPerTargetCommandRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PackagesPerTargetCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-software-packages-per-targets"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PackagesPerTargetCommandReply(**resp)
