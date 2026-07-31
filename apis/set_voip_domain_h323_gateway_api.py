from aiohttp import ClientSession

from config import Config
from models.voip_gateway_reply import VoipGatewayReply
from models.voip_gateway_request_edit import VoipGatewayRequestEdit


async def set_voip_domain_h323_gateway(
    client: ClientSession, data: VoipGatewayRequestEdit, config: Config, **kwargs
) -> VoipGatewayReply:
    """
    Edit existing VoIP Domain H.323 Gateway using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : VoipGatewayRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

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
