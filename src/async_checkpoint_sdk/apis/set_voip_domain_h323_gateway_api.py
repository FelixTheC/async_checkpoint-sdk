from aiohttp import ClientSession

from async_checkpoint_sdk.models.voip_gateway_reply import VoipGatewayReply
from async_checkpoint_sdk.models.voip_gateway_request_edit import VoipGatewayRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_voip_domain_h323_gateway(
    client: ClientSession, data: VoipGatewayRequestEdit, config: SDKConfig, **kwargs
) -> VoipGatewayReply:
    """
    Edit existing VoIP Domain H.323 Gateway using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : VoipGatewayRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    VoipGatewayReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-voip-domain-h323-gateway"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VoipGatewayReply(**resp)
