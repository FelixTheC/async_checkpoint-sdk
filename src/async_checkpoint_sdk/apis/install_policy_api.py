from aiohttp import ClientSession

from async_checkpoint_sdk.models.policy_installation_reply import PolicyInstallationReply
from async_checkpoint_sdk.models.policy_installation_request import PolicyInstallationRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def install_policy(
    client: ClientSession, data: PolicyInstallationRequest, config: SDKConfig, **kwargs
) -> PolicyInstallationReply:
    """
    Executes the install-policy on a given list of targets.

    Parameters
    ----------
    client : ClientSession
    data : PolicyInstallationRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    PolicyInstallationReply

    """
    url = f"https://{config.server}:{config.port}/web_api/install-policy"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PolicyInstallationReply(**resp)
