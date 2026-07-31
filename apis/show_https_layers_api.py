from config import Config
from aiohttp import ClientSession
from models.api_query_request import ApiQueryRequest
from models.t_l_s_layers_query_reply import TLSLayersQueryReply


async def show_https_layers(
    client: ClientSession, data: ApiQueryRequest, config: Config, **kwargs
) -> TLSLayersQueryReply:
    """
    Retrieve all HTTPS Inspection layers.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TLSLayersQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-https-layers"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TLSLayersQueryReply(**resp)
