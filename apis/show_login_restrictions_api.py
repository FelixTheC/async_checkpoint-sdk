from config import Config
from aiohttp import ClientSession
from models.login_restrictions_reply import LoginRestrictionsReply
from models.login_restrictions_request_show import LoginRestrictionsRequestShow


async def show_login_restrictions(
    client: ClientSession, data: LoginRestrictionsRequestShow, config: Config, **kwargs
) -> LoginRestrictionsReply:
    """
    Retrieve existing login restrictions.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : LoginRestrictionsRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
