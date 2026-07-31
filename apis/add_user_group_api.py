from aiohttp import ClientSession

from config import Config
from models.user_group_reply import UserGroupReply
from models.user_group_request_new import UserGroupRequestNew


async def add_user_group(
    client: ClientSession, data: UserGroupRequestNew, config: Config, **kwargs
) -> UserGroupReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : UserGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UserGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-user-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UserGroupReply(**resp)
