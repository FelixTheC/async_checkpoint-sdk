from config import Config
from aiohttp import ClientSession
from models.threat_layer_reply import ThreatLayerReply
from models.threat_layer_request_edit import ThreatLayerRequestEdit


async def set_threat_layer(
    client: ClientSession, data: ThreatLayerRequestEdit, config: Config, **kwargs
) -> ThreatLayerReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatLayerRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatLayerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-threat-layer"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatLayerReply(**resp)
