from config import Config
from aiohttp import ClientSession
from models.application_site_request_edit import ApplicationSiteRequestEdit
from models.application_site_reply import ApplicationSiteReply


async def clone_application_site(
    client: ClientSession, data: ApplicationSiteRequestEdit, config: Config, **kwargs
) -> ApplicationSiteReply:
    """
    Clone existing object.
    
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
    url = f"https://{config.server}:{config.port}/web_api/clone-application-site"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApplicationSiteReply(**resp)
