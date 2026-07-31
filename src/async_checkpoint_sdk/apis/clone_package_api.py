from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.policy_package_request_clone import PolicyPackageRequestClone
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_package(
    client: ClientSession, data: PolicyPackageRequestClone, config: SDKConfig, **kwargs
) -> ApiTaskReply:
    """
    Clone existing policy package using policy name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : PolicyPackageRequestClone [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-package"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
