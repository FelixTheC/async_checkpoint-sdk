from config import Config
from aiohttp import ClientSession
from models.nat_section_identifier_request import NatSectionIdentifierRequest
from models.nat_section_reply import NatSectionReply


async def show_nat_section(
    client: ClientSession, data: NatSectionIdentifierRequest, config: Config, **kwargs
) -> NatSectionReply:
    """
    Retrieve existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : NatSectionIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NatSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-nat-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NatSectionReply(**resp)
