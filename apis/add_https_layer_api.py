from config import Config
from aiohttp import ClientSession
from models.https_layer_reply import HttpsLayerReply
from models.https_layer_request_new import HttpsLayerRequestNew


async def add_https_layer(
    client: ClientSession, data: HttpsLayerRequestNew, config: Config, **kwargs
) -> HttpsLayerReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : HttpsLayerRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    HttpsLayerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-https-layer"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return HttpsLayerReply(**resp)
