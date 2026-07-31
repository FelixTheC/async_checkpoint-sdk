from aiohttp import ClientSession

from async_checkpoint_sdk.models.user_reply import UserReply
from async_checkpoint_sdk.models.user_request_edit import UserRequestEdit
from config import Config


async def set_user(
    client: ClientSession, data: UserRequestEdit, config: Config, **kwargs
) -> UserReply:
    """
    Edit existing object using object name or uid.

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
    url = f"https://{config.server}:{config.port}/web_api/set-user"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UserReply(**resp)
