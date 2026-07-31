from aiohttp import ClientSession

from async_checkpoint_sdk.models.login_restrictions_reply import LoginRestrictionsReply
from async_checkpoint_sdk.models.login_restrictions_request_edit import (
    LoginRestrictionsRequestEdit,
)
from config import Config


async def set_login_restrictions(
    client: ClientSession, data: LoginRestrictionsRequestEdit, config: Config, **kwargs
) -> LoginRestrictionsReply:
    """
    Set login restrictions.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LoginRestrictionsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LoginRestrictionsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-login-restrictions"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LoginRestrictionsReply(**resp)
