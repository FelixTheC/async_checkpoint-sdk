from aiohttp import ClientSession

from async_checkpoint_sdk.models.packages_query_reply import PackagesQueryReply
from async_checkpoint_sdk.models.policy_package_query_request import PolicyPackageQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_packages(
    client: ClientSession, data: PolicyPackageQueryRequest, config: SDKConfig, **kwargs
) -> PackagesQueryReply:
    """
    Retrieve all objects.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : PolicyPackageQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PackagesQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-packages"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PackagesQueryReply(**resp)
