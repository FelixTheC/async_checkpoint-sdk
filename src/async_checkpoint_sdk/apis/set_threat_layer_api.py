from aiohttp import ClientSession

from async_checkpoint_sdk.models.threat_layer_reply import ThreatLayerReply
from async_checkpoint_sdk.models.threat_layer_request_edit import ThreatLayerRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_threat_layer(
    client: ClientSession, data: ThreatLayerRequestEdit, config: SDKConfig, **kwargs
) -> ThreatLayerReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ThreatLayerRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
