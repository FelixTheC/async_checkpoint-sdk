from aiohttp import ClientSession

from config import Config
from models.voip_gatekeeper_reply import VoipGatekeeperReply
from models.voip_gatekeeper_request_new import VoipGatekeeperRequestNew


async def add_voip_domain_h323_gatekeeper(
    client: ClientSession, data: VoipGatekeeperRequestNew, config: Config, **kwargs
) -> VoipGatekeeperReply:
    """
    Create new VoIP Domain H.323 Gatekeeper.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : VoipGatekeeperRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VoipGatekeeperReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-voip-domain-h323-gatekeeper"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VoipGatekeeperReply(**resp)
