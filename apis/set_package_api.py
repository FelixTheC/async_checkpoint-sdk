from config import Config
from aiohttp import ClientSession
from models.policy_package_reply import PolicyPackageReply
from models.policy_package_request_edit import PolicyPackageRequestEdit


async def set_package(
    client: ClientSession, data: PolicyPackageRequestEdit, config: Config, **kwargs
) -> PolicyPackageReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : PolicyPackageRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PolicyPackageReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-package"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PolicyPackageReply(**resp)
