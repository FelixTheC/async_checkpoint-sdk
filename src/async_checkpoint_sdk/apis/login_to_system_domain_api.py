from aiohttp import ClientSession

from async_checkpoint_sdk.models.login_to_system_domain_reply import LoginToSystemDomainReply
from async_checkpoint_sdk.models.login_to_system_domain_request import LoginToSystemDomainRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def login_to_system_domain(
    client: ClientSession, data: LoginToSystemDomainRequest, config: SDKConfig, **kwargs
) -> LoginToSystemDomainReply:
    """
    Login to system domain session from user domain session.

    Parameters
    ----------
    client : ClientSession
    data : LoginToSystemDomainRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LoginToSystemDomainReply

    """
    url = f"https://{config.server}:{config.port}/web_api/login-to-system-domain"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LoginToSystemDomainReply(**resp)
