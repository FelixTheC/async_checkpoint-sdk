from aiohttp import ClientSession

from async_checkpoint_sdk.models.change_password_on_next_login_reply import (
    ChangePasswordOnNextLoginReply,
)
from async_checkpoint_sdk.models.change_password_on_next_login_request import (
    ChangePasswordOnNextLoginRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def change_password_on_next_login(
    client: ClientSession, data: ChangePasswordOnNextLoginRequest, config: SDKConfig, **kwargs
) -> ChangePasswordOnNextLoginReply:
    """
    Change Check Point password on next login.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ChangePasswordOnNextLoginRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ChangePasswordOnNextLoginReply
    """
    url = f"https://{config.server}:{config.port}/web_api/change-password-on-next-login"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ChangePasswordOnNextLoginReply(**resp)
