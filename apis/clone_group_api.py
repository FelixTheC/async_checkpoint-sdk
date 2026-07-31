from aiohttp import ClientSession

from config import Config
from models.group_reply import GroupReply
from models.group_request_edit import GroupRequestEdit


async def clone_group(
    client: ClientSession, data: GroupRequestEdit, config: Config, **kwargs
) -> GroupReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GroupReply(**resp)
