from config import Config
from aiohttp import ClientSession
from models.group_with_exclusion_request_new import GroupWithExclusionRequestNew
from models.group_with_exclusion_reply import GroupWithExclusionReply


async def add_group_with_exclusion(
    client: ClientSession, data: GroupWithExclusionRequestNew, config: Config, **kwargs
) -> GroupWithExclusionReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GroupWithExclusionRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GroupWithExclusionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-group-with-exclusion"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GroupWithExclusionReply(**resp)
