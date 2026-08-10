from aiohttp import ClientSession

from async_checkpoint_sdk.models.policy_package_reply import PolicyPackageReply
from async_checkpoint_sdk.models.policy_package_show_request import PolicyPackageShowRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_package(
    client: ClientSession, data: PolicyPackageShowRequest, config: SDKConfig, **kwargs
) -> PolicyPackageReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : PolicyPackageShowRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
