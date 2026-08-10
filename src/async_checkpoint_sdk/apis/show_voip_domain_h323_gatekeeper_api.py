from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.voip_gatekeeper_reply import VoipGatekeeperReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_voip_domain_h323_gatekeeper(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> VoipGatekeeperReply:
    """
    Retrieve existing VoIP Domain H.323 Gatekeeper using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ApiVisualCPObjectIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    VoipGatekeeperReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-voip-domain-h323-gatekeeper"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VoipGatekeeperReply(**resp)
