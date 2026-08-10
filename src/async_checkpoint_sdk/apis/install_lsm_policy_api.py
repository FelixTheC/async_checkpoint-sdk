from aiohttp import ClientSession

from async_checkpoint_sdk.models.lsm_base_command_reply import LsmBaseCommandReply
from async_checkpoint_sdk.models.lsm_install_policy_request import LsmInstallPolicyRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def install_lsm_policy(
    client: ClientSession, data: LsmInstallPolicyRequest, config: SDKConfig, **kwargs
) -> LsmBaseCommandReply:
    """
    Executes the lsm-install-policy on a given list of targets. Install the LSM policy that defined on the attached LSM profile on the targets devices.

    Parameters
    ----------
    client : ClientSession
    data : LsmInstallPolicyRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LsmBaseCommandReply

    """
    url = f"https://{config.server}:{config.port}/web_api/install-lsm-policy"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LsmBaseCommandReply(**resp)
