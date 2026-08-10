from aiohttp import ClientSession

from async_checkpoint_sdk.models.login_token_reply import LoginTokenReply
from async_checkpoint_sdk.models.login_token_request import LoginTokenRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def get_login_token(
    client: ClientSession, data: LoginTokenRequest, config: SDKConfig, **kwargs
) -> LoginTokenReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : LoginTokenRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
