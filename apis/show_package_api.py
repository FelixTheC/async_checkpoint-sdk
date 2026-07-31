from aiohttp import ClientSession

from config import Config
from models.policy_package_reply import PolicyPackageReply
from models.policy_package_show_request import PolicyPackageShowRequest


async def show_package(
    client: ClientSession, data: PolicyPackageShowRequest, config: Config, **kwargs
) -> PolicyPackageReply:
    """
    Retrieve existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : PolicyPackageShowRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PolicyPackageReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-package"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PolicyPackageReply(**resp)
