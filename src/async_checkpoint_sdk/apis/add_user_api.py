from aiohttp import ClientSession

from async_checkpoint_sdk.models.user_reply import UserReply
from async_checkpoint_sdk.models.user_request_new import UserRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_user(
    client: ClientSession, data: UserRequestNew, config: SDKConfig, **kwargs
) -> UserReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : UserRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UserReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-user"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UserReply(**resp)
