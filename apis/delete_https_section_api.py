from aiohttp import ClientSession

from config import Config
from models.api_ok_reply import ApiOkReply
from models.t_l_s_section_identifier_request import TLSSectionIdentifierRequest


async def delete_https_section(
    client: ClientSession, data: TLSSectionIdentifierRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete existing HTTPS Inspection section using section name or uid and layer name.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TLSSectionIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-https-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
