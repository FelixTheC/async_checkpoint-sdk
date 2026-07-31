from aiohttp import ClientSession

from async_checkpoint_sdk.models.deployment_command_reply import DeploymentCommandReply
from async_checkpoint_sdk.models.deployment_command_request_verify import (
    DeploymentCommandRequestVerify,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def verify_software_package(
    client: ClientSession, data: DeploymentCommandRequestVerify, config: SDKConfig, **kwargs
) -> DeploymentCommandReply:
    """
    Verifies the software package on target machines.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DeploymentCommandRequestVerify [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DeploymentCommandReply
    """
    url = f"https://{config.server}:{config.port}/web_api/verify-software-package"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DeploymentCommandReply(**resp)
