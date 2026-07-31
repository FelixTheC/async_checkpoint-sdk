from config import Config
from aiohttp import ClientSession
from models.access_section_reply import AccessSectionReply
from models.access_section_identifier_request import AccessSectionIdentifierRequest


async def show_access_section(
    client: ClientSession, data: AccessSectionIdentifierRequest, config: Config, **kwargs
) -> AccessSectionReply:
    """
    Retrieve existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AccessSectionIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AccessSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-access-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessSectionReply(**resp)
