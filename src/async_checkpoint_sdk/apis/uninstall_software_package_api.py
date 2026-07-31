from aiohttp import ClientSession

from async_checkpoint_sdk.models.deployment_command_reply import DeploymentCommandReply
from async_checkpoint_sdk.models.deployment_command_request import DeploymentCommandRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def uninstall_software_package(
    client: ClientSession, data: DeploymentCommandRequest, config: SDKConfig, **kwargs
) -> DeploymentCommandReply:
    """
    Uninstalls the software package from target machines.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DeploymentCommandRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DeploymentCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/uninstall-software-package"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DeploymentCommandReply(**resp)
