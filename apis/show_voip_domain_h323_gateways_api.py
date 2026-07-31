from aiohttp import ClientSession

from config import Config
from models.api_query_object_reply import ApiQueryObjectReply
from models.api_query_request import ApiQueryRequest


async def show_voip_domain_h323_gateways(
    client: ClientSession, data: ApiQueryRequest, config: Config, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all VoIP Domain H.323 Gateways.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-voip-domain-h323-gateways"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
