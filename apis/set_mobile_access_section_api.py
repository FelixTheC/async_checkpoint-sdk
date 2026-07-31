from config import Config
from aiohttp import ClientSession
from models.mobile_applications_section_request_edit import MobileApplicationsSectionRequestEdit
from models.mobile_applications_section_reply import MobileApplicationsSectionReply


async def set_mobile_access_section(
    client: ClientSession, data: MobileApplicationsSectionRequestEdit, config: Config, **kwargs
) -> MobileApplicationsSectionReply:
    """
    Edit existing Mobile Access section using section name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileApplicationsSectionRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileApplicationsSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-mobile-access-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileApplicationsSectionReply(**resp)
