from aiohttp import ClientSession

from async_checkpoint_sdk.models.user_reply import UserReply
from async_checkpoint_sdk.models.user_request_edit import UserRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_user(
    client: ClientSession, data: UserRequestEdit, config: SDKConfig, **kwargs
) -> UserReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : UserRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
