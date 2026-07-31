from config import Config
from aiohttp import ClientSession
from models.login_token_request import LoginTokenRequest
from models.login_token_reply import LoginTokenReply


async def get_login_token(
    client: ClientSession, data: LoginTokenRequest, config: Config, **kwargs
) -> LoginTokenReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : LoginTokenRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LoginTokenReply
    """
    url = f"https://{config.server}:{config.port}/web_api/get-login-token"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LoginTokenReply(**resp)
