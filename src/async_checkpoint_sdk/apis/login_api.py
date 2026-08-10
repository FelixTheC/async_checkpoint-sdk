from aiohttp import ClientSession

from async_checkpoint_sdk.models.web_api_login_reply import WebApiLoginReply
from async_checkpoint_sdk.models.web_api_login_request import WebApiLoginRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def login(
    client: ClientSession, data: WebApiLoginRequest, config: SDKConfig, **kwargs
) -> WebApiLoginReply:
    """
    Log in to the server with username and password. The server shows your session unique identifier. Enter this session unique identifier in the 'X-chkp-sid' header of each request.

    Parameters
    ----------
    client : ClientSession
    data : WebApiLoginRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    WebApiLoginReply

    """
    url = f"https://{config.server}:{config.port}/web_api/login"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WebApiLoginReply(**resp)
