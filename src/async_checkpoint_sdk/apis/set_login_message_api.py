from aiohttp import ClientSession

from async_checkpoint_sdk.models.login_message_reply import LoginMessageReply
from async_checkpoint_sdk.models.login_message_request_set import LoginMessageRequestSet
from config import Config


async def set_login_message(
    client: ClientSession, data: LoginMessageRequestSet, config: Config, **kwargs
) -> LoginMessageReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LoginMessageRequestSet [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LoginMessageReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-login-message"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LoginMessageReply(**resp)
