from aiohttp import ClientSession

from config import Config
from models.access_section_identifier_request import AccessSectionIdentifierRequest
from models.api_ok_reply import ApiOkReply


async def delete_access_section(
    client: ClientSession, data: AccessSectionIdentifierRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AccessSectionIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-access-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
