from config import Config
from aiohttp import ClientSession
from models.lsm_install_policy_request import LsmInstallPolicyRequest
from models.lsm_base_command_reply import LsmBaseCommandReply


async def install_lsm_policy(
    client: ClientSession, data: LsmInstallPolicyRequest, config: Config, **kwargs
) -> LsmBaseCommandReply:
    """
    Executes the lsm-install-policy on a given list of targets. Install the LSM policy that defined on the attached LSM profile on the targets devices.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : LsmInstallPolicyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
