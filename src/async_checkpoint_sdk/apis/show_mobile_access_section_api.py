from aiohttp import ClientSession

from async_checkpoint_sdk.models.mobile_applications_section_identifier_request_show import (
    MobileApplicationsSectionIdentifierRequestShow,
)
from async_checkpoint_sdk.models.mobile_applications_section_reply import (
    MobileApplicationsSectionReply,
)
from config import Config


async def show_mobile_access_section(
    client: ClientSession,
    data: MobileApplicationsSectionIdentifierRequestShow,
    config: Config,
    **kwargs,
) -> MobileApplicationsSectionReply:
    """
    Retrieve existing Mobile Access section using section name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileApplicationsSectionIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileApplicationsSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-mobile-access-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileApplicationsSectionReply(**resp)
