from aiohttp import ClientSession

from async_checkpoint_sdk.models.application_site_group_reply import ApplicationSiteGroupReply
from async_checkpoint_sdk.models.application_site_group_request_new import (
    ApplicationSiteGroupRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_application_site_group(
    client: ClientSession, data: ApplicationSiteGroupRequestNew, config: SDKConfig, **kwargs
) -> ApplicationSiteGroupReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApplicationSiteGroupRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApplicationSiteGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-application-site-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApplicationSiteGroupReply(**resp)
