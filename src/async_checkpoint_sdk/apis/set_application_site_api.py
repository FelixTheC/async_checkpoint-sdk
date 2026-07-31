from aiohttp import ClientSession

from async_checkpoint_sdk.models.application_site_reply import ApplicationSiteReply
from async_checkpoint_sdk.models.application_site_request_edit import ApplicationSiteRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_application_site(
    client: ClientSession, data: ApplicationSiteRequestEdit, config: SDKConfig, **kwargs
) -> ApplicationSiteReply:
    """
    Edit existing application using object name or uid. It's impossible to set 'application-signature' when the application was initialized with 'url-list' and vice-verse.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApplicationSiteRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApplicationSiteReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-application-site"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApplicationSiteReply(**resp)
