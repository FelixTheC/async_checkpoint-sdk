from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.sip_proxy_reply import SipProxyReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_voip_domain_sip_proxy(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> SipProxyReply:
    """
    Retrieve existing VoIP Domain SIP Proxy using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : ApiVisualCPObjectIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    SipProxyReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-voip-domain-sip-proxy"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SipProxyReply(**resp)
