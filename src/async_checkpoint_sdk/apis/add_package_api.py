from aiohttp import ClientSession

from async_checkpoint_sdk.models.policy_package_reply import PolicyPackageReply
from async_checkpoint_sdk.models.policy_package_request_new import PolicyPackageRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_package(
    client: ClientSession, data: PolicyPackageRequestNew, config: SDKConfig, **kwargs
) -> PolicyPackageReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : PolicyPackageRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PolicyPackageReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-package"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PolicyPackageReply(**resp)
