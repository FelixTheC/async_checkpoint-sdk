from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.mobile_profile_section_identifier_request_show import (
    MobileProfileSectionIdentifierRequestShow,
)
from config import Config


async def delete_mobile_access_profile_section(
    client: ClientSession, data: MobileProfileSectionIdentifierRequestShow, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete existing Mobile Access Profile section using section name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileProfileSectionIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-mobile-access-profile-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
