from aiohttp import ClientSession

from config import Config
from models.application_site_reply import ApplicationSiteReply
from models.application_site_request_new import ApplicationSiteRequestNew


async def add_application_site(
    client: ClientSession, data: ApplicationSiteRequestNew, config: Config, **kwargs
) -> ApplicationSiteReply:
    """
    Creates new application site, which can be initialized with 'url-list' or 'application-signature' (not both of them).
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApplicationSiteRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApplicationSiteReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-application-site"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApplicationSiteReply(**resp)
