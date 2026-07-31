from config import Config
from aiohttp import ClientSession
from models.t_l_s_section_identifier_request import TLSSectionIdentifierRequest
from models.t_l_s_section_reply import TLSSectionReply


async def show_https_section(
    client: ClientSession, data: TLSSectionIdentifierRequest, config: Config, **kwargs
) -> TLSSectionReply:
    """
    Retrieve existing HTTPS Inspection section using section name or uid and layer name.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TLSSectionIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TLSSectionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-https-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TLSSectionReply(**resp)
