from aiohttp import ClientSession

from async_checkpoint_sdk.models.web_api_logout_reply import WebApiLogoutReply
from async_checkpoint_sdk.models.web_api_logout_request import WebApiLogoutRequest
from config import Config


async def logout(
    client: ClientSession, data: WebApiLogoutRequest, config: Config, **kwargs
) -> WebApiLogoutReply:
    """
    Log out from the current session. After logging out the session id is not valid any more.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : WebApiLogoutRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WebApiLogoutReply
    """
    url = f"https://{config.server}:{config.port}/web_api/logout"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WebApiLogoutReply(**resp)
