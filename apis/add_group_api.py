from config import Config
from aiohttp import ClientSession
from models.group_request_new import GroupRequestNew
from models.group_reply import GroupReply


async def add_group(
    client: ClientSession, data: GroupRequestNew, config: Config, **kwargs
) -> GroupReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GroupReply(**resp)
