from config import Config
from aiohttp import ClientSession
from models.policy_installation_reply import PolicyInstallationReply
from models.policy_installation_request import PolicyInstallationRequest


async def install_policy(
    client: ClientSession, data: PolicyInstallationRequest, config: Config, **kwargs
) -> PolicyInstallationReply:
    """
    Executes the install-policy on a given list of targets.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : PolicyInstallationRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
