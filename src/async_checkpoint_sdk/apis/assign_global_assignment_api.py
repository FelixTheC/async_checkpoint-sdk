from aiohttp import ClientSession

from async_checkpoint_sdk.models.assign_global_policy_reply import AssignGlobalPolicyReply
from async_checkpoint_sdk.models.assign_global_policy_request import AssignGlobalPolicyRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def assign_global_assignment(
    client: ClientSession, data: AssignGlobalPolicyRequest, config: SDKConfig, **kwargs
) -> AssignGlobalPolicyReply:
    """
    Executes the assign-global-assignment from a given list of global-domains to a given list of dependent-domains.

    Parameters
    ----------
    client : ClientSession
    data : AssignGlobalPolicyRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    AssignGlobalPolicyReply

    """
    url = f"https://{config.server}:{config.port}/web_api/assign-global-assignment"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AssignGlobalPolicyReply(**resp)
