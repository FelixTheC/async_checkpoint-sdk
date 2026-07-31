from config import Config
from aiohttp import ClientSession
from models.https_layer_reply import HttpsLayerReply
from models.t_l_s_layer_request_edit import TLSLayerRequestEdit


async def set_https_layer(
    client: ClientSession, data: TLSLayerRequestEdit, config: Config, **kwargs
) -> HttpsLayerReply:
    """
    Edit existing HTTPS Inspection layer using layer name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TLSLayerRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    HttpsLayerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-https-layer"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return HttpsLayerReply(**resp)
