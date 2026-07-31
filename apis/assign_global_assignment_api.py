from aiohttp import ClientSession

from config import Config
from models.assign_global_policy_reply import AssignGlobalPolicyReply
from models.assign_global_policy_request import AssignGlobalPolicyRequest


async def assign_global_assignment(
    client: ClientSession, data: AssignGlobalPolicyRequest, config: Config, **kwargs
) -> AssignGlobalPolicyReply:
    """
    Executes the assign-global-assignment from a given list of global-domains to a given list of dependent-domains.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AssignGlobalPolicyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
