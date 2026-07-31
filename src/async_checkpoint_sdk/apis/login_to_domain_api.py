from aiohttp import ClientSession

from async_checkpoint_sdk.models.login_to_domain_request import LoginToDomainRequest
from async_checkpoint_sdk.models.web_api_login_reply import WebApiLoginReply
from config import Config


async def login_to_domain(
    client: ClientSession, data: LoginToDomainRequest, config: Config, **kwargs
) -> WebApiLoginReply:
    """
    Login from MDS to other domain.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LoginToDomainRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WebApiLoginReply
    """
    url = f"https://{config.server}:{config.port}/web_api/login-to-domain"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WebApiLoginReply(**resp)
