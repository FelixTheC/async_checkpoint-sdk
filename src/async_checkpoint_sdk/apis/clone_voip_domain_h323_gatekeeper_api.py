from aiohttp import ClientSession

from async_checkpoint_sdk.models.voip_gatekeeper_reply import VoipGatekeeperReply
from async_checkpoint_sdk.models.voip_gatekeeper_request_edit import VoipGatekeeperRequestEdit
from config import Config


async def clone_voip_domain_h323_gatekeeper(
    client: ClientSession, data: VoipGatekeeperRequestEdit, config: Config, **kwargs
) -> VoipGatekeeperReply:
    """
    Clone existing VoIP Domain H.323 Gatekeeper.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : VoipGatekeeperRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VoipGatekeeperReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-voip-domain-h323-gatekeeper"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VoipGatekeeperReply(**resp)
