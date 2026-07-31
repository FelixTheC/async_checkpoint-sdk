from aiohttp import ClientSession

from config import Config
from models.user_group_reply import UserGroupReply
from models.user_group_request_edit import UserGroupRequestEdit


async def clone_user_group(
    client: ClientSession, data: UserGroupRequestEdit, config: Config, **kwargs
) -> UserGroupReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : UserGroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UserGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-user-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UserGroupReply(**resp)
