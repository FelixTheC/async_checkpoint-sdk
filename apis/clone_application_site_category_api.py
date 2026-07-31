from config import Config
from aiohttp import ClientSession
from models.application_site_category_request_edit import ApplicationSiteCategoryRequestEdit
from models.application_site_category_reply import ApplicationSiteCategoryReply


async def clone_application_site_category(
    client: ClientSession, data: ApplicationSiteCategoryRequestEdit, config: Config, **kwargs
) -> ApplicationSiteCategoryReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApplicationSiteCategoryRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApplicationSiteCategoryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-application-site-category"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApplicationSiteCategoryReply(**resp)
