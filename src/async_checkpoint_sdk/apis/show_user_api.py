from aiohttp import ClientSession

from async_checkpoint_sdk.models.user_reply import UserReply
from async_checkpoint_sdk.models.user_request_show import UserRequestShow
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_user(
    client: ClientSession, data: UserRequestShow, config: SDKConfig, **kwargs
) -> UserReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : UserRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UserReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-user"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UserReply(**resp)
