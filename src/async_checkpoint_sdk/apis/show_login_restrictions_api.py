from aiohttp import ClientSession

from async_checkpoint_sdk.models.login_restrictions_reply import LoginRestrictionsReply
from async_checkpoint_sdk.models.login_restrictions_request_show import (
    LoginRestrictionsRequestShow,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_login_restrictions(
    client: ClientSession, data: LoginRestrictionsRequestShow, config: SDKConfig, **kwargs
) -> LoginRestrictionsReply:
    """
    Retrieve existing login restrictions.

    Parameters
    ----------
    client : ClientSession
    data : LoginRestrictionsRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LoginRestrictionsReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-login-restrictions"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LoginRestrictionsReply(**resp)
