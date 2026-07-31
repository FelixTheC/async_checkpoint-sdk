from aiohttp import ClientSession

from async_checkpoint_sdk.models.voip_gateway_reply import VoipGatewayReply
from async_checkpoint_sdk.models.voip_gateway_request_new import VoipGatewayRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_voip_domain_h323_gateway(
    client: ClientSession, data: VoipGatewayRequestNew, config: SDKConfig, **kwargs
) -> VoipGatewayReply:
    """
    Create new VoIP Domain H.323 Gateway.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : VoipGatewayRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VoipGatewayReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-voip-domain-h323-gateway"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VoipGatewayReply(**resp)
