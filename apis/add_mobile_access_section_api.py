from aiohttp import ClientSession

from config import Config
from models.mobile_applications_section_reply import MobileApplicationsSectionReply
from models.mobile_applications_section_request_new import MobileApplicationsSectionRequestNew


async def add_mobile_access_section(
    client: ClientSession, data: MobileApplicationsSectionRequestNew, config: Config, **kwargs
) -> MobileApplicationsSectionReply:
    """
    Create new Mobile Access section.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileApplicationsSectionRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileApplicationsSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-mobile-access-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileApplicationsSectionReply(**resp)
