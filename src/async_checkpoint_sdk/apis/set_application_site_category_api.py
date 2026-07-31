from aiohttp import ClientSession

from async_checkpoint_sdk.models.application_site_category_reply import (
    ApplicationSiteCategoryReply,
)
from async_checkpoint_sdk.models.application_site_category_request_edit import (
    ApplicationSiteCategoryRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_application_site_category(
    client: ClientSession, data: ApplicationSiteCategoryRequestEdit, config: SDKConfig, **kwargs
) -> ApplicationSiteCategoryReply:
    """
    Edit existing object using object name or uid.

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
    url = f"https://{config.server}:{config.port}/web_api/set-application-site-category"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApplicationSiteCategoryReply(**resp)
