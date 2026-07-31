from config import Config
from aiohttp import ClientSession
from models.application_site_request_edit import ApplicationSiteRequestEdit
from models.application_site_reply import ApplicationSiteReply


async def set_application_site(
    client: ClientSession, data: ApplicationSiteRequestEdit, config: Config, **kwargs
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
