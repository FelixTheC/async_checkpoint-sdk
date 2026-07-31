from config import Config
from aiohttp import ClientSession
from models.voip_gateway_reply import VoipGatewayReply
from models.voip_gateway_request_new import VoipGatewayRequestNew


async def add_voip_domain_h323_gateway(
    client: ClientSession, data: VoipGatewayRequestNew, config: Config, **kwargs
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
