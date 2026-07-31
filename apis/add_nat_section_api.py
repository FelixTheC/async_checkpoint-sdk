from aiohttp import ClientSession

from config import Config
from models.nat_section_reply import NatSectionReply
from models.nat_section_request_new import NatSectionRequestNew


async def add_nat_section(
    client: ClientSession, data: NatSectionRequestNew, config: Config, **kwargs
) -> NatSectionReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : NatSectionRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NatSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-nat-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NatSectionReply(**resp)
