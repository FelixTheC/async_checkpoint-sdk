from aiohttp import ClientSession

from async_checkpoint_sdk.models.web_api_logout_reply import WebApiLogoutReply
from async_checkpoint_sdk.models.web_api_logout_request import WebApiLogoutRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def logout(
    client: ClientSession, config: SDKConfig, **kwargs
) -> WebApiLogoutReply:
    """
    Log out from the current session. After logging out the session id is not valid any more.

    Parameters
    ----------
    client : ClientSession
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    WebApiLogoutReply

    """
    url = f"https://{config.server}:{config.port}/web_api/logout"
    async with client.post(url, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WebApiLogoutReply(**resp)
