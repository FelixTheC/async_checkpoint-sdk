from aiohttp import ClientSession

from async_checkpoint_sdk.models.application_site_category_reply import (
    ApplicationSiteCategoryReply,
)
from async_checkpoint_sdk.models.application_site_category_request_new import (
    ApplicationSiteCategoryRequestNew,
)
from config import Config


async def add_application_site_category(
    client: ClientSession, data: ApplicationSiteCategoryRequestNew, config: Config, **kwargs
) -> ApplicationSiteCategoryReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApplicationSiteCategoryRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApplicationSiteCategoryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-application-site-category"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApplicationSiteCategoryReply(**resp)
