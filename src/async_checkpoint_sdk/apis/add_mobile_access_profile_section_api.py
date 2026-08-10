from aiohttp import ClientSession

from async_checkpoint_sdk.models.mobile_profile_section_reply import MobileProfileSectionReply
from async_checkpoint_sdk.models.mobile_profile_section_request_new import (
    MobileProfileSectionRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_mobile_access_profile_section(
    client: ClientSession, data: MobileProfileSectionRequestNew, config: SDKConfig, **kwargs
) -> MobileProfileSectionReply:
    """
    Create new Mobile Access Profile section.

    Parameters
    ----------
    client : ClientSession
    data : MobileProfileSectionRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MobileProfileSectionReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-mobile-access-profile-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileProfileSectionReply(**resp)
