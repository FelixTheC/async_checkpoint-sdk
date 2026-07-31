from aiohttp import ClientSession

from async_checkpoint_sdk.models.voip_gatekeeper_reply import VoipGatekeeperReply
from async_checkpoint_sdk.models.voip_gatekeeper_request_edit import VoipGatekeeperRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_voip_domain_h323_gatekeeper(
    client: ClientSession, data: VoipGatekeeperRequestEdit, config: SDKConfig, **kwargs
) -> VoipGatekeeperReply:
    """
    Edit existing VoIP Domain H.323 Gatekeeper using object name or uid.

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
    url = f"https://{config.server}:{config.port}/web_api/set-voip-domain-h323-gatekeeper"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VoipGatekeeperReply(**resp)
