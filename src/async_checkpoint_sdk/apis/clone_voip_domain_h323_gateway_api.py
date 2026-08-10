from aiohttp import ClientSession

from async_checkpoint_sdk.models.voip_gateway_reply import VoipGatewayReply
from async_checkpoint_sdk.models.voip_gateway_request_edit import VoipGatewayRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_voip_domain_h323_gateway(
    client: ClientSession, data: VoipGatewayRequestEdit, config: SDKConfig, **kwargs
) -> VoipGatewayReply:
    """
    Clone existing VoIP Domain H.323 Gateway.

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
    url = f"https://{config.server}:{config.port}/web_api/clone-voip-domain-h323-gateway"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VoipGatewayReply(**resp)
