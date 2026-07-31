from aiohttp import ClientSession

from async_checkpoint_sdk.models.application_site_group_reply import ApplicationSiteGroupReply
from async_checkpoint_sdk.models.application_site_group_request_edit import (
    ApplicationSiteGroupRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_application_site_group(
    client: ClientSession, data: ApplicationSiteGroupRequestEdit, config: SDKConfig, **kwargs
) -> ApplicationSiteGroupReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApplicationSiteGroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApplicationSiteGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-application-site-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApplicationSiteGroupReply(**resp)
