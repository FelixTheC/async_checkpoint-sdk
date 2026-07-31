from aiohttp import ClientSession

from async_checkpoint_sdk.models.mobile_profile_section_reply import MobileProfileSectionReply
from async_checkpoint_sdk.models.mobile_profile_section_request_edit import (
    MobileProfileSectionRequestEdit,
)
from config import Config


async def set_mobile_access_profile_section(
    client: ClientSession, data: MobileProfileSectionRequestEdit, config: Config, **kwargs
) -> MobileProfileSectionReply:
    """
    Edit existing Mobile Access Profile section using section name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileProfileSectionRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileProfileSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-mobile-access-profile-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileProfileSectionReply(**resp)
