from config import Config
from aiohttp import ClientSession
from models.user_request_edit import UserRequestEdit
from models.user_reply import UserReply


async def clone_user(
    client: ClientSession, data: UserRequestEdit, config: Config, **kwargs
) -> UserReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : UserRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UserReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-user"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UserReply(**resp)
