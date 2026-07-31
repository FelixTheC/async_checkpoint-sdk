from aiohttp import ClientSession

from async_checkpoint_sdk.models.user_group_reply import UserGroupReply
from async_checkpoint_sdk.models.user_group_request_edit import UserGroupRequestEdit
from config import Config


async def set_user_group(
    client: ClientSession, data: UserGroupRequestEdit, config: Config, **kwargs
) -> UserGroupReply:
    """
    Edit existing object using object name or uid.

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
    url = f"https://{config.server}:{config.port}/web_api/set-user-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UserGroupReply(**resp)
