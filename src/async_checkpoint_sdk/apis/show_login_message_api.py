from aiohttp import ClientSession

from async_checkpoint_sdk.models.login_message_reply import LoginMessageReply
from async_checkpoint_sdk.models.login_message_request_show import LoginMessageRequestShow
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_login_message(
    client: ClientSession, data: LoginMessageRequestShow, config: SDKConfig, **kwargs
) -> LoginMessageReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : LoginMessageRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LoginMessageReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-login-message"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LoginMessageReply(**resp)
